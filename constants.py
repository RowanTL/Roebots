import numpy as np

Backleg_amplitude = np.pi / 4
Backleg_frequency = 6
Backleg_phaseOffset = np.pi / 4
Frontleg_amplitude = np.pi / 4
Frontleg_frequency = 6
Frontleg_phaseOffset = 0

Torso_Backleg_max_force = 50
Torso_Frontleg_max_force = 50

gravity = 9.8

# loop controls
iter_amt = 1000
sleep_time = 1/70