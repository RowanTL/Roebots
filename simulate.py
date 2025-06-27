"""import pybullet as p
import pybullet_data
from time import sleep
import pyrosim.pyrosim as pyrosim
import numpy as np
import random
from constants import *

# on the manylinks section at the moment
physicsClient = p.connect(p.GUI)
p.configureDebugVisualizer(p.COV_ENABLE_GUI,0)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-gravity)
robotId = p.loadURDF("body.urdf")
planeId = p.loadURDF("plane.urdf")
p.loadSDF("world.sdf")

pyrosim.Prepare_To_Simulate(robotId)

backlegSensorValues = np.zeros(iter_amt)
frontlegSensorValues = np.zeros(iter_amt)
Backleg_targetAngles = Backleg_amplitude * np.sin(Backleg_frequency * np.linspace(0, 2 * np.pi, iter_amt) + Backleg_phaseOffset)
Frontleg_targetAngles = Frontleg_amplitude * np.sin(Frontleg_frequency * np.linspace(0, 2 * np.pi, iter_amt) + Frontleg_phaseOffset)

#np.save("data/BacklegtargetAngles.npy", Backleg_targetAngles)
#np.save("data/FrontlegtargetAngles.npy", Frontleg_targetAngles)
#exit()

for n in range(iter_amt):
    p.stepSimulation()
    # touch sensors only work with non-root links

    # motors always attached to joints and not links
    pyrosim.Set_Motor_For_Joint(
        bodyIndex = robotId,
        jointName = "Torso_Backleg",
        controlMode = p.POSITION_CONTROL,
        targetPosition = Backleg_targetAngles[n],
        maxForce = Torso_Backleg_max_force
    )
    pyrosim.Set_Motor_For_Joint(
        bodyIndex=robotId,
        jointName="Torso_Frontleg",
        controlMode=p.POSITION_CONTROL,
        targetPosition=Frontleg_targetAngles[n],
        maxForce=Torso_Frontleg_max_force
    )
    backlegSensorValues[n] = pyrosim.Get_Touch_Sensor_Value_For_Link("Backleg")
    frontlegSensorValues[n] = pyrosim.Get_Touch_Sensor_Value_For_Link("Frontleg")
    sleep(sleep_time)

print(backlegSensorValues)
np.save("data/backlegSensor.npy", backlegSensorValues)
np.save("data/frontlegSensor.npy", frontlegSensorValues)
p.disconnect()"""
import pybullet as p
import pybullet_data
from world import WORLD
from robot import ROBOT
from constants import *
from time import sleep

class SIMULATION:
    def __init__(self):
        physicsClient = p.connect(p.GUI)
        p.configureDebugVisualizer(p.COV_ENABLE_GUI, 0)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0, 0, -gravity)

        self.world = WORLD()
        self.robot = ROBOT()

        self.Run()

    def Run(self):
        for n in range(iter_amt):
            p.stepSimulation()
            # touch sensors only work with non-root links
            self.robot.Sense(n)
            self.robot.Act(n)

            # motors always attached to joints and not links
            """pyrosim.Set_Motor_For_Joint(
                bodyIndex=self.robot.robotId,
                jointName="Torso_Backleg",
                controlMode=p.POSITION_CONTROL,
                targetPosition=Backleg_targetAngles[n],
                maxForce=Torso_Backleg_max_force
            )
            pyrosim.Set_Motor_For_Joint(
                bodyIndex=robotId,
                jointName="Torso_Frontleg",
                controlMode=p.POSITION_CONTROL,
                targetPosition=Frontleg_targetAngles[n],
                maxForce=Torso_Frontleg_max_force
            )
            backlegSensorValues[n] = pyrosim.Get_Touch_Sensor_Value_For_Link("Backleg")
            frontlegSensorValues[n] = pyrosim.Get_Touch_Sensor_Value_For_Link("Frontleg")"""
            sleep(sleep_time)

    # destructor
    def __del__(self):
        p.disconnect()

simulation = SIMULATION()