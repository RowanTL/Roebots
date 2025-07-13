from motor import MOTOR
from sensor import SENSOR
from pyrosim import pyrosim
from pyrosim.neuralNetwork import NEURAL_NETWORK
import pybullet as p
import os

class ROBOT:
    def __init__(self, solutionID: str):
        self.motors = {}
        self.sensors = {}
        self.nn = NEURAL_NETWORK(f"brain{solutionID}.nndf")

        # delete the brainID.nndf file no reduce bloat
        os.system(f"rm brain{solutionID}.nndf")

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
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                desiredAngle = self.nn.Get_Value_Of(neuronName)
                motor = self.motors[jointName]
                motor.Set_Value(self.robotId, desiredAngle)

    def Think(self):
        self.nn.Update()
        #self.nn.Print()

    def Get_Fitness(self, solutionID: str):
        stateOfLinkZero = p.getLinkState(self.robotId, 0)
        positionOfLinkZero = stateOfLinkZero[0]
        xCoordinateOfLinkZero = positionOfLinkZero[0]
        with open(f"tmp{solutionID}.txt", 'w') as file:
            file.write(str(xCoordinateOfLinkZero))
        os.system(f"mv tmp{solutionID}.txt fitness{solutionID}.txt")