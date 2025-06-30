from constants import *
from pyrosim import pyrosim
import pybullet as p

class MOTOR:
    def __init__(self, jointname):
        self.jointname = jointname

    def Set_Value(self, robotId, desiredAngle: int):
        pyrosim.Set_Motor_For_Joint(
            bodyIndex=robotId,
            jointName=self.jointname,
            controlMode=p.POSITION_CONTROL,
            targetPosition=desiredAngle,
            maxForce=Torso_Backleg_max_force
        )