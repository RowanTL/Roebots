import pybullet as p
import pybullet_data
from time import sleep
import pyrosim.pyrosim as pyrosim
import numpy as np

# on the manylinks section at the moment
physicsClient = p.connect(p.GUI)
p.configureDebugVisualizer(p.COV_ENABLE_GUI,0)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)
robotId = p.loadURDF("body.urdf")
planeId = p.loadURDF("plane.urdf")
p.loadSDF("world.sdf")

pyrosim.Prepare_To_Simulate(robotId)

iter_amt: int = 100
backlegSensorValues = np.zeros(iter_amt)

for n in range(iter_amt):
    p.stepSimulation()
    # touch sensors only work with non-root links
    backlegSensorValues[n] = pyrosim.Get_Touch_Sensor_Value_For_Link("Backleg")
    sleep((1/70))

print(backlegSensorValues)
np.save("data/backlegSensor.npy", backlegSensorValues)
p.disconnect()
