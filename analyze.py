import numpy as np
import matplotlib.pyplot as plt

backlegSensorValues = np.load("data/backlegSensor.npy")
frontlegSensorValues = np.load("data/frontlegSensor.npy")
targetAngles = np.load("data/targetAngles.npy")
backlegTargetAngles = np.load("data/BacklegtargetAngles.npy")
frontlegTargetAngles = np.load("data/FrontlegtargetAngles.npy")
#print(backlegSensorValues)

"""plt.figure(figsize=(10, 6))

plt.subplot(2, 1, 1)
plt.plot(backlegSensorValues, color='blue')
plt.title("Backleg Sensor Values")
plt.xlabel("Time Step")
plt.ylabel("Sensor Reading")
plt.grid(True)

plt.subplot(2, 1, 2)
plt.plot(frontlegSensorValues, color='green')
plt.title("Frontleg Sensor Values")
plt.xlabel("Time Step")
plt.ylabel("Sensor Reading")
plt.grid(True)

plt.tight_layout()
plt.show()

plt.plot(targetAngles, color='green')
plt.show()"""

plt.plot(backlegTargetAngles, color='red')
plt.plot(frontlegTargetAngles, color='blue')
plt.show()