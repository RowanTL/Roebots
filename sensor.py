import numpy as np
from constants import *
from pyrosim import pyrosim

class SENSOR:
    def __init__(self, linkname):
        self.values = np.zeros(iter_amt)
        self.linkname = linkname

    def Get_Value(self, t: int):
        self.values[t] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkname)
        #if t == iter_amt - 1:
        #    print(self.values)

    def Save_Values(self):
        np.save(f"data/{self.linkname}Sensor.npy", self.values)