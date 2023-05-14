import numpy as np
from autolab_core import RigidTransform
from frankapy import FrankaArm
from enum import Enum
import rospy
from geometry_msgs.msg import Pose
from sandwich_robot.msg import object_pose

class States(Enum):
    IDLE = 0
    FORWARD_MODE = 1
    RESET_MODE = 2

class SandwichMaker:
    def __init__(self):
        self.fa = FrankaArm()
        self.fa.reset_joints()
        rospy.Subscriber("/object_transform_publisher", object_pose, self.callback)

        self.state = States.IDLE
        
        self.pick_x = None
        self.pick_y = None
        self.pick_z = None

        self.place_x = None
        self.place_y = None
        self.place_z = None

    def callback(self, pose):
        try:
            self.tomato_pos = [pose.x_pose[0], pose.y_pose[0]]
            self.top_bun_pos = [pose.x_pose[1], pose.y_pose[1]]
            self.base_bun_pos = [pose.x_pose[2], pose.y_pose[2]]

        except IndexError:
            pass


    def pick(self):

        self.fa.open_gripper()

        des_pose = RigidTransform(rotation=np.array([
        [1.0, 0.0, 0.0],
        [0.0, -1.0, 0.0],
        [0.0, 0.0, -1.0]]),
        translation = np.array([self.pick_x, self.pick_y, self.pick_z + 0.015]),
        from_frame = 'franka_tool', to_frame='world')

        self.fa.goto_pose(des_pose,duration=5.0,use_impedance=False)

        des_pose = RigidTransform(rotation=np.array([
        [1.0, 0.0, 0.0],
        [0.0, -1.0, 0.0],
        [0.0, 0.0, -1.0]]),
        translation = np.array([self.pick_x, self.pick_y, self.pick_z]),
        from_frame = 'franka_tool', to_frame='world')

        self.fa.goto_pose(des_pose,duration=1.0,use_impedance=False)
        self.fa.close_gripper()
        

    def place(self):
        des_pose = RigidTransform(rotation=np.array([
            [1.0, 0.0, 0.0],
            [0.0, -1.0, 0.0],
            [0.0, 0.0, -1.0]]),
            translation = np.array([self.place_x, self.place_y, self.place_z]),
            from_frame = 'franka_tool', to_frame='world')

        self.fa.goto_pose(des_pose,duration = 5.0, use_impedance=False)

        self.fa.open_gripper()

    def pick_manager(self, item_number):

        if self.state == States.FORWARD_MODE:
            self.pick_z = 0.01

            if item_number == 0:
                print("Picking Base Bun")
                self.pick_x = self.base_bun_pos[0]
                self.pick_y = self.base_bun_pos[1]
                self.pick()

            elif item_number == 1:
                print("Picking Tomato")
                self.pick_x = self.tomato_pos[0]
                self.pick_y = self.tomato_pos[1]
                self.pick()

            elif item_number == 2:
                print("Picking Top Bun")
                self.pick_x = self.top_bun_pos[0]
                self.pick_y = self.top_bun_pos[1]
                self.pick()

        elif self.state == States.RESET_MODE:

            if item_number == 2:
                print("Picking Top Bun")
                self.pick_x = self.top_bun_pos[0]
                self.pick_y = self.top_bun_pos[1]
                self.pick_z = 0.012*(item_number - 1.5 +1)+0.015
                self.pick()

            elif item_number == 1:
                print("Picking Tomato")
                self.pick_x = self.tomato_pos[0]
                self.pick_y = self.tomato_pos[1]
                self.pick_z = 0.012*(item_number - 1.5 +1)+0.015 - 0.005
                self.pick()

            elif item_number == 0:
                print("Picking Bun")
                self.pick_x = self.base_bun_pos[0]
                self.pick_y = self.base_bun_pos[1]
                self.pick_z = 0.012*(item_number - 1.5 +1)+0.015
                self.pick()


    def place_manager(self, item_number):

        if self.state == States.FORWARD_MODE:

            self.place_x = 0.35
            self.place_y = 0

            if item_number == 0:
                print("Placing Base Bun")
                self.place_z = 0.012*(item_number - 0.1 +1)+0.015 - 0.01
                self.place()

            elif item_number == 1:
                print("Placing Tomato")
                self.place_z = 0.012*(item_number - 0.1 +1)+0.015 - 0.01
                self.place()

            elif item_number == 2:
                print("Placing Top Bun")
                self.place_z = 0.012*(item_number - 0.1 +1)+0.015 - 0.01
                self.place()

        elif self.state == States.RESET_MODE:
            
            if item_number == 2:
                print("Placing Top Bun")

            elif item_number == 1:
                print("Placing Tomato")

            elif item_number == 0:
                print("Placing Base Bun")

            self.place_x = 0.35+(item_number/10)
            self.place_y = -0.25
            self.place_z = 0.01
            self.place()



    def reset_pose(self):
        
        des_pose = RigidTransform(rotation=np.array([
            [1.0, 0.0, 0.0],
            [0.0, -1.0, 0.0],
            [0.0, 0.0, -1.0]]),
            translation = np.array([0.35, 0.0, 0.35]),
            from_frame = 'franka_tool', to_frame='world')

        self.fa.goto_pose(des_pose,duration=5.0, use_impedance=False)



    def pick_back(self,box_number):
        if box_number == -0.5:
            des_pose = RigidTransform(rotation=np.array([
                [1.0, 0.0, 0.0],
                [0.0, -1.0, 0.0],
                [0.0, 0.0, -1.0]]),
                translation = np.array([self.des_x, self.des_y, (0.012*(box_number+1)+0.015 - 0.005)]),
                from_frame = 'franka_tool', to_frame='world')        
        else:
            des_pose = RigidTransform(rotation=np.array([
                [1.0, 0.0, 0.0],
                [0.0, -1.0, 0.0],
                [0.0, 0.0, -1.0]]),
                translation = np.array([0.35, 0, (0.012*(box_number+1)+0.015)]),
                from_frame = 'franka_tool', to_frame='world')

        self.fa.goto_pose(des_pose,duration = 5.0, use_impedance=False)

        self.fa.close_gripper()    

    def place_back(self, position):

        des_pose = RigidTransform(rotation=np.array([
            [1.0, 0.0, 0.0],
            [0.0, -1.0, 0.0],
            [0.0, 0.0, -1.0]]),
            translation = np.array([0.35+(position/10), -0.25, 0.01]),
            from_frame = 'franka_tool', to_frame='world')

        self.fa.goto_pose(des_pose,duration=5.0,use_impedance=False)

        self.fa.open_gripper()


    def forward_mode(self, number_of_items):

        rospy.Subscriber("/object_transform_publisher", object_pose, self.callback)
            
        self.state = States.FORWARD_MODE

        for i in range(number_of_items):
    
            self.pick_manager(i)
            self.reset_pose()              
            self.place_manager(i)
            self.reset_pose()

    def reset_mode(self, number_of_items):

        rospy.Subscriber("/object_transform_publisher", object_pose, self.callback)
        self.state = States.RESET_MODE

        for i in range(number_of_items-1,-1,-1):

            self.fa.open_gripper()
            self.pick_manager(i)
            self.reset_pose()              
            self.place_manager(i)
            self.reset_pose()




if __name__ == "__main__":

    sw = SandwichMaker()           #instantiate sandwich maker class

    try:
        sw.build_order()
    
    except Exception as e:
        print(e)