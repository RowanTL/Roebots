import random

import numpy as np
from pyrosim import pyrosim
import os
from pathlib import Path
from time import sleep

x = 0
y = 0
z = 0.5
s = 1  # size for later

class SOLUTION:
    def __init__(self, myID: int):
        self.weights = np.random.rand(3, 2)
        self.weights = self.weights * 2 - 1
        self.myID = myID
        self.fitnessFile = f"fitness{myID}.txt"

    def Start_Simulation(self, directOrGui: str):
        self.Create_World()
        self.Create_Body()
        self.Create_Brain(self.myID)

        os.system(f"python3 simulate.py {directOrGui} {self.myID} 2&>1 &")

    def Wait_For_Simulation_To_End(self):
        while not Path(self.fitnessFile).exists():
            sleep(0.01)
        with open(self.fitnessFile, 'r') as file:
            self.fitness = float(file.read())
        Path(self.fitnessFile).unlink(missing_ok=True)

    def Evaluate(self, directOrGui: str):
        """
        This function might be slated for deletion later.
        Still used in a call in the code.

        :param directOrGui:
        :return:
        """
        self.Create_World()
        self.Create_Body()
        self.Create_Brain(self.myID)

        os.system(f"python3 simulate.py {directOrGui} {self.myID} &")
        while not Path(self.fitnessFile).exists():
            sleep(0.01)
        with open(self.fitnessFile, 'r') as file:
            self.fitness = float(file.read())
        print("----------------------------", self.fitness)

    def Mutate(self):
        randomRow = random.randint(0, 2)
        randomColumn = random.randint(0, 1)
        self.weights[randomRow][randomColumn] = random.random() * 2 - 1


    def Create_Brain(self, solutionID: int):
        pyrosim.Start_NeuralNetwork(f"brain{solutionID}.nndf")
        pyrosim.Send_Sensor_Neuron(name=0, linkName="Torso")
        pyrosim.Send_Sensor_Neuron(name=1, linkName="Backleg")
        pyrosim.Send_Sensor_Neuron(name=2, linkName="Frontleg")
        pyrosim.Send_Motor_Neuron(name=3, jointName="Torso_Backleg")
        pyrosim.Send_Motor_Neuron(name=4, jointName="Torso_Frontleg")
        for currentRow in [0, 1, 2]:
            for currentColumn in [0, 1]:
                pyrosim.Send_Synapse(sourceNeuronName=currentRow, targetNeuronName=currentColumn + 3, weight=self.weights[currentRow][currentColumn])
        pyrosim.End()

    def Create_Body(self):
        pyrosim.Start_URDF("body.urdf")
        pyrosim.Send_Cube(name="Torso", pos=[0, 0, 1.5], size=[1, 1, 1])
        pyrosim.Send_Joint(name="Torso_Backleg", child="Backleg", parent="Torso", type="revolute",
                           position=[-0.5, 0, 1])
        pyrosim.Send_Cube(name="Backleg", pos=[-0.5, 0, -0.5], size=[1, 1, 1])
        pyrosim.Send_Joint(name="Torso_Frontleg", child="Frontleg", parent="Torso", type="revolute",
                           position=[0.5, 0, 1])
        pyrosim.Send_Cube(name="Frontleg", pos=[0.5, 0, -0.5])
        pyrosim.End()

    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")
        pyrosim.Send_Cube(name=f"Box", pos=[x + 4, y + 4, z], size=[s, s, s])
        pyrosim.End()

    def Set_ID(self, newID: int):
        self.myID = newID