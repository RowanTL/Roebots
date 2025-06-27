from motor import MOTOR
from sensor import SENSOR
from pyrosim import pyrosim
import pybullet as p

class ROBOT:
    def __init__(self):
        self.motors = {}
        self.sensors = {}

        self.robotId = p.loadURDF("body.urdf")
        pyrosim.Prepare_To_Simulate(self.robotId)
        self.Prepare_To_Sense()
        self.Prepare_To_Act()

    def Prepare_To_Sense(self):
        for linkname in pyrosim.linkNamesToIndices:
            self.sensors[linkname] = SENSOR(linkname)

    def Sense(self, t: int):
        """

        :param t: The time step to modify
        :return:
        """
        for sensor in self.sensors.values():
            sensor.Get_Value(t)

    def Prepare_To_Act(self):
        for linkname in pyrosim.jointNamesToIndices:
            self.motors[linkname] = MOTOR(linkname)

    def Act(self, t: int):
        for motor in self.motors.values():
            motor.Set_Value(self.robotId, t)