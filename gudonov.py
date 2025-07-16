import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import matplotlib as mpl
import math

dt = 0.005
dx = 0.02
T = 1000
X = 500
x_0 = -5.0

#Sets initial data
def InitialData():
  u_l = 0.7
  u_m = 0.7
  u_r = 0.5
  initial_values = []
  #for x in range(X):
    #if (x_0 + (dx * x)) <= -1.0 :
      #initial_values.append(u_l)
    #elif (x_0 + (dx * x)) <= 1.0 :
      #initial_values.append(u_m)
    #else :
      #initial_values.append(u_r)
  for x in range(X):
    initial_values.append(math.sin(8*x*math.pi/X)*0.5+0.5)
  return initial_values

#This evaluates the numeric flux as if the flux function is f(u)=u(1-u)
#Currently all except the final "else" statement will hold for concave functions
def NumericFlux(u_l,u_r):
  if (u_l < u_r) and (Flux(u_l) <= Flux(u_r)):
    return Flux(u_l)
  elif (u_l < u_r):
    return Flux(u_r)
  elif (FluxDerivative(u_l) >= 0):
    return Flux(u_l)
  elif (FluxDerivative(u_r) <= 0):
    return Flux(u_r)
  else:
    return Flux(0.5) #in this case, the value of the flux function at the critical point is returned
    
def LaxIncrementTimestep(current_data):
  new_data = []
  for x in range(X):
    if x == 0 :
      new_data.append(0.5*(current_data[x]+current_data[x+1])-0.5*(dt/dx)*(Flux(current_data[x+1])-Flux(current_data[x])))
    elif x == X-1:
      new_data.append(0.5*(current_data[x-1]+current_data[x])-0.5*(dt/dx)*(Flux(current_data[x])-Flux(current_data[x-1])))
    else :
      new_data.append(0.5*(current_data[x-1]+current_data[x+1])-0.5*(dt/dx)*(Flux(current_data[x+1])-Flux(current_data[x-1])))
  return new_data

def Flux(u):
  return u*(1.0-u)

def FluxDerivative(u):
  return 1.0-2.0*u
  
#Takes the input of current data and outputs resulting data of next timestep
def GudonovIncrementTimestep(current_data):
  new_data = []
  for x in range(X):
    #Special Cases for when x=0 and x=X
    if x == 0 :
      new_data.append(current_data[x] - (dt/dx)*(NumericFlux(current_data[x],current_data[x+1])-Flux(current_data[x])))
    elif x == X-1 :
      new_data.append(current_data[x] - (dt/dx)*(Flux(current_data[x])-NumericFlux(current_data[x-1],current_data[x])))
    else :
      new_data.append(current_data[x] - (dt/dx)*(NumericFlux(current_data[x],current_data[x+1])-NumericFlux(current_data[x-1],current_data[x])))
  return new_data

#Main
gudonov_final_data = []
gudonov_current_data = InitialData()
gudonov_final_data.append(gudonov_current_data.copy())
for t in range(T-1):
  gudonov_current_data = GudonovIncrementTimestep(gudonov_current_data)
  gudonov_final_data.append(gudonov_current_data.copy())
lax_final_data = []
lax_current_data = InitialData()
lax_final_data.append(lax_current_data.copy())
for t in range(T-1):
  lax_current_data = LaxIncrementTimestep(lax_current_data)
  lax_final_data.append(lax_current_data.copy())
fig, ax = plt.subplots(nrows=1,ncols=2)
ax[0].set_title('Gudonov')
heatmap0 = ax[0].imshow(gudonov_final_data,"plasma")
plt.colorbar(heatmap0)
ax[1].set_title('Lax-Friedrichs')
heatmap1 = ax[1].imshow(lax_final_data)
plt.colorbar(heatmap1)
ax[0].set_xlabel("Position")
ax[0].set_ylabel("Time")
ax[0].axis([0,X,0,T])
ax[1].set_xlabel("Position")
ax[1].set_ylabel("Time")
ax[1].axis([0,X,0,T])
plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=0.5, hspace=None)
plt.savefig("gudonov_plot.png")