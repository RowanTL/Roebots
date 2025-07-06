import random

import numpy as np
from pyrosim import pyrosim
import os

x = 0
y = 0
z = 0.5
s = 1  # size for later

class SOLUTION:
    def __init__(self):
        self.weights = np.random.rand(3, 2)
        self.weights = self.weights * 2 - 1
        self.fitnessFile = "fitness.txt"

    def Evaluate(self):
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()

        os.system("python3 simulate.py")
        with open(self.fitnessFile, 'r') as file:
            self.fitness = float(file.read())

    def Mutate(self):
        randomRow = random.randint(0, 2)
        randomColumn = random.randint(0, 1)
        self.weights[randomRow][randomColumn] = random.random() * 2 - 1


    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork("brain.nndf")
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