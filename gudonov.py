import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

#Sets initial data
def InitialData(params):
  dt = params['dt']
  dx = params['dx']
  X = params['X']
  x_0 = params['x_0']
  u_l = 0.0;
  u_r = 1.0;
  inital_values = []
  for x in range(X):
    if (x_0 + (dx * x)) <= 0) :
      initial_values.append(u_l)
    else :
      initial_values.append(u_r)
  return initial_values

#Takes the input of current data and outputs resulting data of next timestep
def IncrementTimestep(params, current_data):
  dt = params['dt']
  dx = params['dx']
  X = params['X']
  x_0 = params['x_0']

#Parameters for the method; T is the number of total time steps, and X is the total number of cells.
params = {
  'dt' = 0.1
  'dx' = 0.1
  'T' = 20.0
  'X' = 20.0
  'x_0' = -1.0
}

#Main
final_data = []
current_data = InitialData(params)
final_data.append(current_data.copy())
