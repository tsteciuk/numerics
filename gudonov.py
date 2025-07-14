import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import matplotlib as mpl

#Sets initial data
def InitialData(params):
  dt = params['dt']
  dx = params['dx']
  X = params['X']
  x_0 = params['x_0']
  u_l = 0.0
  u_r = 1.0
  inital_values = []
  for x in range(X):
    if (x_0 + (dx * x)) <= 0) :
      initial_values.append(u_l)
    else :
      initial_values.append(u_r)
  return initial_values

#This evaluates the numeric flux as if the flux function is f(u)=u(1-u)
#Currently all except the final "else" statement will hold for concave functions
def NumericFlux(u_l,u_r):
  if (u_l < u_r) and (Flux(u_l) <= Flux(u_r)):
    return Flux(u_l)
  else if (u_l < u_r):
    return Flux(u_r)
  else if (FluxDerivative(u_l) >= 0):
    return Flux(u_l)
  else if (FluxDerivative(u_r) <= 0):
    return Flux(u_r)
  else:
    a = -FluxDerivative(u_l)/(FluxDerivative(u_r)-FluxDerivative(u_l))
    return (1.0-a)*Flux(u_l) + a*Flux(u_r)
    
    

def Flux(u):
  return u*(1.0-u)

def FluxDerivative(u):
  return 1.0-2.0*u
  
#Takes the input of current data and outputs resulting data of next timestep
def IncrementTimestep(params, current_data):
  dt = params['dt']
  dx = params['dx']
  X = params['X']
  x_0 = params['x_0']
  new_data = []
  for x in range(X):
    #Special Cases for when x=0 and x=X
    if x == 0 :
      new_data.append(current_data[x] - (dt/dx)*(NumericFlux(current_data[x],current_data[x+1])-Flux(current_data[x])))
    else if x == X-1 :
      new_data.append(current_data[x] - (dt/dx)*(Flux(current_data[x])-NumericFlux(current_data[x-1],current_data[x])))
    else :
      new_data.append(current_data[x] - (dt/dx)*(NumericFlux(current_data[x],current_data[x+1])-NumericFlux(current_data[x-1],current_data[x])))
  return new_data

#Parameters for the method; T is the number of total time steps, and X is the total number of cells.
params = {
  'dt' = 0.1
  'dx' = 0.1
  'T' = 20
  'X' = 20
  'x_0' = -1.0
}

#Main
final_data = []
current_data = InitialData(params)
final_data.append(current_data.copy())
for t in range(T-1):
  current_data = IncrementTimestep(params, current_data)
  final_data.append(current_data.copy())
fig, ax = plt.subplots()
im = ax.imshow(harvest)
plt.show()
