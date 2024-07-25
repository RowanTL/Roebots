import pybullet as p
import pybullet_data
from time import sleep

# on the manylinks section at the moment
physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
p.loadSDF("boxes.sdf")

for _ in range(2000):
    p.stepSimulation()
    sleep((1/70))

p.disconnect()
