import pybullet as p
import pybullet_data
from time import sleep
import pyrosim.pyrosim as pyrosim
import numpy as np
import math

# on the manylinks section at the moment
physicsClient = p.connect(p.GUI)
p.configureDebugVisualizer(p.COV_ENABLE_GUI,0)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)
robotId = p.loadURDF("body.urdf")
planeId = p.loadURDF("plane.urdf")
p.loadSDF("world.sdf")

pyrosim.Prepare_To_Simulate(robotId)

iter_amt: int = 10000
backlegSensorValues = np.zeros(iter_amt)
frontlegSensorValues = np.zeros(iter_amt)

for n in range(iter_amt):
    p.stepSimulation()
    # touch sensors only work with non-root links

    # motors always attached to joints and not links
    pyrosim.Set_Motor_For_Joint(
        bodyIndex = robotId,
        jointName = "Torso_Backleg",
        controlMode = p.POSITION_CONTROL,
        targetPosition = -math.pi/6.0,
        maxForce = 500
    )
    pyrosim.Set_Motor_For_Joint(
        bodyIndex=robotId,
        jointName="Torso_Frontleg",
        controlMode=p.POSITION_CONTROL,
        targetPosition=math.pi / 6.0,
        maxForce=500
    )
    backlegSensorValues[n] = pyrosim.Get_Touch_Sensor_Value_For_Link("Backleg")
    frontlegSensorValues[n] = pyrosim.Get_Touch_Sensor_Value_For_Link("Frontleg")
    sleep((1/70))

print(backlegSensorValues)
np.save("data/backlegSensor.npy", backlegSensorValues)
np.save("data/frontlegSensor.npy", frontlegSensorValues)
p.disconnect()
