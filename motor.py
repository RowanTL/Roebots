from constants import *
from pyrosim import pyrosim
import pybullet as p

class MOTOR:
    def __init__(self, jointname):
        self.jointname = jointname

        self.Prepare_To_Act()

    def Prepare_To_Act(self):
        self.amplitude = amplitude
        self.frequency = frequency if self.jointname == "Torso_Backleg" else frequency / 2
        self.offset = phaseOffset
        self.targetAngles = self.amplitude * np.sin(
            self.frequency * np.linspace(0, 2 * np.pi, iter_amt) + self.offset)

    def Set_Value(self, robotId, desiredAngle: int):
        pyrosim.Set_Motor_For_Joint(
            bodyIndex=robotId,
            jointName=self.jointname,
            controlMode=p.POSITION_CONTROL,
            targetPosition=desiredAngle,
            maxForce=Torso_Backleg_max_force
        )

    def Save_Values(self):
        np.save(f"data/{self.jointname}Angles.npy", self.targetAngles)