import pyrosim.pyrosim as pyrosim

x = 0
y = 0
z = 0.5

pyrosim.Start_SDF("box.sdf")
pyrosim.Send_Cube(name="Box", pos=[x,y,z] , size=[1,1,1])
pyrosim.Send_Cube(name="Box2", pos=[1,0,1.5] , size=[1,1,1])
pyrosim.End()
