import os
import time
import numpy as np

from MIDAS.enums import *
from MIDAS.engine import PolarGrid, Engine

os.system('clear')

# === Parameters ===========================================================

# movieDir = project.root + '/Movies/TAPAs/'

# === Engine ===============================================================

E = Engine()
# E = Engine(arena=Arena.CIRCULAR)

# Number of steps
E.steps = None

# Verbose
# E.verbose.level = Verbose.HIGH

# E.verbose('outside')

# === Agents ===============================================================

# --- Fixed agents ---------------------------------------------------------

# E.add_group(Agent.BLIND, Nagents, name='agents', 
#             anoise = 0.1,
#             vnoise = 0.001)

# --- RIPO agents ----------------------------------------------------------

# polar grid
G = PolarGrid(rZ=[0], nSa = 4)

coeffs = np.array([1,1,1,1, 0, 0, 0, 0])*1

#  --- Inputs
in_presence = E.add_input(Perception.PRESENCE,
                          normalization = Normalization.NONE,
                          grid = G,
                          coefficients = coeffs)

# in_orientation = E.add_input(Perception.ORIENTATION, 
#                             normalization = Normalization.NONE,
#                             grid = G,
#                             coefficients = [1, 1, 1, 1, 0, 0, 0, 18])

# --- Outputs 

out_da = E.add_output(Action.REORIENTATION,
                      activation = Activation.ANGLE)

# out_dv = E.add_output(Action.SPEED_MODULATION,
#                       activation = Activation.SPEED)

# Initial conditions
N = 100
IC = {'position': None,
      'orientation': None,
      'speed': 0.005} 

# IC = {'position': [[0,0], [0.2,0.3]],
#       'orientation': [1.5, 0],
#       'speed': 0.015}
# N = len(IC['position']) 

E.add_group(Agent.RIPO, N, name='agents',
            initial_condition = IC,
            rmax = None, 
            damax = np.pi/6,           
            inputs=[in_presence], outputs=[out_da])

# === Storage ==============================================================

# E.setup_storage('/home/raphael/Science/Projects/CM/MovingAgents/Data/RIPO/test.db')

# === Visualization ========================================================

E.setup_animation()
E.animation.options['agents']['cmap'] = 'hsv'

# --- Information

# E.animation.add_info_weights()
# E.animation.add_info()

# --- Traces
# E.animation.trace_duration = 10

# === Simulation ===========================================================

# E.window.autoplay = False
# E.window.movieFile = movieDir + 'test.mp4'

E.run()