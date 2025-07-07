import pybullet as p
import pybullet_data
from world import WORLD
from robot import ROBOT
from constants import *
from time import sleep
import sys

class SIMULATION:
    def __init__(self, directOrGui: str):
        #physicsClient = p.connect(p.GUI)
        if directOrGui == "GUI":
            physicsClient = p.connect(p.GUI)
        else:
            hysicsClient = p.connect(p.DIRECT)
        p.configureDebugVisualizer(p.COV_ENABLE_GUI, 0)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0, 0, -gravity)

        self.directOrGui = directOrGui
        self.world = WORLD()
        self.robot = ROBOT()

        self.Run()

    def Run(self):
        for n in range(iter_amt):
            p.stepSimulation()
            # touch sensors only work with non-root links
            self.robot.Sense(n)
            self.robot.Think()
            self.robot.Act(n)

            # motors always attached to joints and not links
            if self.directOrGui == "GUI":
                sleep(sleep_time)

    # destructor
    def __del__(self):
        p.disconnect()

    def Get_Fitness(self):
        self.robot.Get_Fitness()

simulation = SIMULATION(sys.argv[1])
simulation.Get_Fitness()