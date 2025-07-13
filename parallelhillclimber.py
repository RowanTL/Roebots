from solution import SOLUTION
from constants import *
import copy
import os

class PARALLEL_HILL_CLIMBER:
    def __init__(self):
        os.system("rm brain*.nndf") # if any of these files exist, could cause issues
        os.system("rm fitness*.txt")

        self.parents: dict = {}
        self.nextAvailableID = 0
        for n in range(populationSize):
            self.parents[n] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1

    def Spawn(self):
        self.children: dict = {}
        for key in self.parents.keys():
            self.children[key] = copy.deepcopy(self.parents[key])
            #self.children[key].Set_ID(self.nextAvailableID)
            #self.nextAvailableID += 1
        #self.child = copy.deepcopy(self.parent)
        #self.child.Set_ID(self.nextAvailableID)
        #self.nextAvailableID += 1

    def Mutate(self):
        for child in self.children.values():
            child.Mutate()

    def Select(self):
        for key in self.parents.keys():
            if self.children[key].fitness > self.parents[key].fitness:
                self.parents[key] = self.children[key]

    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children)
        self.Print()
        self.Select()

    def Evolve(self):
        """self.parent.Evaluate("DIRECT")
        os.system("python simulate.py GUI")
        for currentGeneration in range(numberOfGenerations):
            self.Evolve_For_One_Generation()"""
        self.Evaluate(self.parents)
        for currentGeneration in range(numberOfGenerations):
            self.Evolve_For_One_Generation()

    def Evaluate(self, solutions: dict):
        for n in range(populationSize):
            solutions[n].Start_Simulation("DIRECT")
        for n in range(populationSize):
            solutions[n].Wait_For_Simulation_To_End()

    def Show_Best(self):
        sorted_parents = sorted(self.parents.values(), key=lambda item: item.fitness, reverse=True)
        sorted_parents[0].Start_Simulation("GUI")

    def Print(self):
        print()
        for key in self.parents:
            print(f"parent {key} fitness: {self.parents[key].fitness}, child {key} fitness: {self.children[key].fitness}")
        print()