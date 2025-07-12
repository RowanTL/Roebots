import numpy as np

amplitude = np.pi / 4
frequency = 6
phaseOffset = np.pi / 4
#Frontleg_amplitude = np.pi / 4
#Frontleg_frequency = 6
#Frontleg_phaseOffset = 0

Torso_Backleg_max_force = 50
Torso_Frontleg_max_force = 50

gravity = 9.8

# simulation loop controls
iter_amt = 500
sleep_time = 1/140

# evolutionary run loop controls
numberOfGenerations = 17
populationSize = 2