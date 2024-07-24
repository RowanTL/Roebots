import pybullet as p
from time import sleep

physicsClient = p.connect(p.GUI)

for _ in range(1000):
    p.stepSimulation()
    sleep((1/70))

p.disconnect()
