import pybullet as p
from time import sleep

physicsClient = p.connect(p.GUI)
p.setGravity(0,0,-9.8)
p.loadSDF("box.sdf")

for _ in range(1000):
    p.stepSimulation()
    sleep((1/70))

p.disconnect()
