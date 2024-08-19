import pyrosim.pyrosim as pyrosim

x = 0
y = 0
z = 0.5
s = 1  # size for later

"""def Create_Robot():
    pyrosim.Start_URDF("body.urdf")
    pyrosim.Send_Cube(name="Link0", pos=[x,y,z] , size=[s,s,s])
    pyrosim.Send_Joint( name = "Link0_Link1" , parent= "Link0" , child = "Link1" , type = "revolute", position = [0,0,1])
    pyrosim.Send_Cube(name="Link1", pos=[0,0,0.5], size=[s,s,s])
    pyrosim.Send_Joint( name = "Link1_Link2" , parent= "Link1" , child = "Link2" , type = "revolute", position = [0,0,1])
    pyrosim.Send_Cube(name="Link2", pos=[0,0,0.5], size=[s,s,s])
    pyrosim.Send_Joint(name="Link2_Link3", parent="Link2", child="Link3", type="revolute", position=[0,0.5,0.5])
    pyrosim.Send_Cube(name="Link3", pos=[0,0.5,0], size=[s,s,s])
    pyrosim.Send_Joint(name="Link3_Link4", parent="Link3", child="Link4", type="revolute", position=[0,1,0])
    pyrosim.Send_Cube(name="Link4", pos=[0,0.5,0], size=[s,s,s])
    pyrosim.Send_Joint(name="Link4_Link5", parent="Link4", child="Link5", type="revolute", position=[0,0.5,-0.5])
    pyrosim.Send_Cube(name="Link5", pos=[0,0,-0.5], size=[s,s,s])
    pyrosim.Send_Joint(name="Link5_Link6", parent="Link5", child="Link6", type="revolute", position=[0,0,-1])
    pyrosim.Send_Cube(name="Link6", pos=[0,0,-0.5], size=[s,s,s])
    pyrosim.End()"""

# Assignment code for joints
def Create_Robot():
    pyrosim.Start_URDF("body.urdf")
    pyrosim.Send_Cube(name="Torso", pos=[0,0,1.5], size=[1,1,1])
    pyrosim.Send_Joint(name="Torso_Backleg", child="Backleg", parent="Torso", type="revolute", position=[-0.5,0,1])
    pyrosim.Send_Cube(name="Backleg", pos=[-0.5,0,-0.5], size=[1,1,1])
    pyrosim.Send_Joint(name="Backleg_Frontleg", child="Frontleg", parent="Torso", type="revolute", position=[0.5,0,1])
    pyrosim.Send_Cube(name="Frontleg", pos=[0.5,0,-0.5])
    pyrosim.End()

def Create_World():
    pyrosim.Start_SDF("world.sdf")
    pyrosim.Send_Cube(name=f"Box", pos=[x + 4,y + 4,z] , size=[s,s,s])
    pyrosim.End()

Create_World()
Create_Robot()
