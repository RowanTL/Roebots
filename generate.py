import pyrosim.pyrosim as pyrosim

x = 0
y = 0
z = 0.5
s = 1  # size for later

pyrosim.Start_SDF("boxes.sdf")
for n in range(10):
    pyrosim.Send_Cube(name=f"Box{n}", pos=[x,y,z] , size=[s,s,s])
    z += 1
    s *= .9

pyrosim.End()
