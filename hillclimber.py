from solution import SOLUTION
from constants import *
import copy
import os

class HILL_CLIMBER:
    def __init__(self):
        self.parent = SOLUTION()

    def Spawn(self):
        self.child = copy.deepcopy(self.parent)

    def Mutate(self):
        self.child.Mutate()

    def Select(self):
        if self.child.fitness > self.parent.fitness:
            self.parent = self.child

    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.child.Evaluate("DIRECT")
        print(f"parent fitness: {self.parent.fitness}, child fitness: {self.child.fitness}")
        self.Select()

    def Evolve(self):
        self.parent.Evaluate("DIRECT")
        os.system("python simulate.py GUI")
        for currentGeneration in range(numberOfGenerations):
            self.Evolve_For_One_Generation()

    def Show_Best(self):
        os.system(f"python3 simulate.py GUI")