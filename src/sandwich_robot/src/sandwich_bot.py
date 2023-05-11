import numpy as np
from autolab_core import RigidTransform
from frankapy import FrankaArm
import rospy
from geometry_msgs.msg import Pose
from sandwich_robot.msg import object_pose


class sandwich_maker:
    def __init__(self):
        fa = FrankaArm()
        fa.reset_joints()
        rospy.Subscriber("/goal_pose", object_pose, self.callback)


    def callback(self,pose):
        # global stop_moving
        # global des_x
        # global des_y


        # self.des_x = pose.position.x
        # self.des_y = pose.position.y
        try:
            self.tomato_pos = [pose.x_pose[0], pose.y_pose[0]]
            self.top_bun_pos = [pose.x_pose[1], pose.y_pose[1]]
            self.base_bun_pos = [pose.x_pose[2], pose.y_pose[2]]
        except IndexError:
            pass


        print("TOM", self.tomato_pos)


    def pick_object(self,position):

        fa.open_gripper()

        if position == 0:
            cur_x = self.base_bun_pos[0]
            cur_y = self.base_bun_pos[1]
            des_pose = RigidTransform(rotation=np.array([
            [1.0, 0.0, 0.0],
            [0.0, -1.0, 0.0],
            [0.0, 0.0, -1.0]]),
            # translation = np.array([0.35+(position/10), -0.25, 0.009]),
            translation = np.array([cur_x, cur_y, 0.025]),
            from_frame = 'franka_tool', to_frame='world')

            fa.goto_pose(des_pose,duration=5.0,use_impedance=False)

            des_pose = RigidTransform(rotation=np.array([
            [1.0, 0.0, 0.0],
            [0.0, -1.0, 0.0],
            [0.0, 0.0, -1.0]]),
            # translation = np.array([0.35+(position/10), -0.25, 0.009]),
            translation = np.array([cur_x, cur_y, 0.01]),
            from_frame = 'franka_tool', to_frame='world')

            fa.goto_pose(des_pose,duration=1.0,use_impedance=False)

        elif position == 1:
            cur_x = self.tomato_pos[0]
            cur_y = self.tomato_pos[1]
            des_pose = RigidTransform(rotation=np.array([
            [1.0, 0.0, 0.0],
            [0.0, -1.0, 0.0],
            [0.0, 0.0, -1.0]]),
            # translation = np.array([0.35+(position/10), -0.25, 0.009]),
            translation = np.array([self.tomato_pos[0], self.tomato_pos[1], 0.025]),
            from_frame = 'franka_tool', to_frame='world')

            fa.goto_pose(des_pose,duration=5.0,use_impedance=False)

            des_pose = RigidTransform(rotation=np.array([
            [1.0, 0.0, 0.0],
            [0.0, -1.0, 0.0],
            [0.0, 0.0, -1.0]]),
            # translation = np.array([0.35+(position/10), -0.25, 0.009]),
            translation = np.array([cur_x, cur_y, 0.006]),
            from_frame = 'franka_tool', to_frame='world')

            fa.goto_pose(des_pose,duration=1.0,use_impedance=False)

        elif position == 2:
            
            cur_x = self.top_bun_pos[0]
            cur_y = self.top_bun_pos[1]
            des_pose = RigidTransform(rotation=np.array([
            [1.0, 0.0, 0.0],
            [0.0, -1.0, 0.0],
            [0.0, 0.0, -1.0]]),
            # translation = np.array([0.35+(position/10), -0.25, 0.009]),
            translation = np.array([cur_x, cur_y, 0.025]),
            from_frame = 'franka_tool', to_frame='world')

            fa.goto_pose(des_pose,duration=5.0,use_impedance=False)

            des_pose = RigidTransform(rotation=np.array([
            [1.0, 0.0, 0.0],
            [0.0, -1.0, 0.0],
            [0.0, 0.0, -1.0]]),
            # translation = np.array([0.35+(position/10), -0.25, 0.009]),
            translation = np.array([cur_x, cur_y, 0.01]),
            from_frame = 'franka_tool', to_frame='world')

            fa.goto_pose(des_pose,duration=1.0,use_impedance=False)

        else:
            print("PICK NOT WORKING")

            # des_pose = RigidTransform(rotation=np.array([
            #     [1.0, 0.0, 0.0],
            #     [0.0, -1.0, 0.0],
            #     [0.0, 0.0, -1.0]]),
            #     translation = np.array([0.35+(position/10), -0.25, 0.01]),
            #     from_frame = 'franka_tool', to_frame='world')

        # fa.goto_pose(des_pose,duration=5.0,use_impedance=False)

        fa.close_gripper()
        


    def reset_pose(self):
        
        des_pose = RigidTransform(rotation=np.array([
            [1.0, 0.0, 0.0],
            [0.0, -1.0, 0.0],
            [0.0, 0.0, -1.0]]),
            translation = np.array([0.35, 0.0, 0.35]),
            from_frame = 'franka_tool', to_frame='world')

        fa.goto_pose(des_pose,duration=5.0, use_impedance=False)


    
    def place_object(self,box_number):
        # print("Item number:" + str(box_number+1))
        des_pose = RigidTransform(rotation=np.array([
            [1.0, 0.0, 0.0],
            [0.0, -1.0, 0.0],
            [0.0, 0.0, -1.0]]),
            translation = np.array([0.35, 0, (0.012*(box_number+1)+0.015 - 0.01)]),
            from_frame = 'franka_tool', to_frame='world')

        fa.goto_pose(des_pose,duration = 5.0, use_impedance=False)

        fa.open_gripper()




    def build_order(self):
        number_of_items = 3             

        while not rospy.is_shutdown():
            print("Making your sandwich")
            for i in range(number_of_items):
        
                self.pick_object(i)
                self.reset_pose()              
                self.place_object(i-0.1)
                self.reset_pose()

            print("Your order is ready")

            print("cancelling order")
            for i in range(number_of_items-1,-1,-1):
            # move_arm()
                fa.open_gripper()
                self.pick_back(i-1.5)
                self.reset_pose()
                self.place_back(i)       
                self.reset_pose()


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

        fa.goto_pose(des_pose,duration = 5.0, use_impedance=False)

        fa.close_gripper()    

    def place_back(self, position):

        des_pose = RigidTransform(rotation=np.array([
            [1.0, 0.0, 0.0],
            [0.0, -1.0, 0.0],
            [0.0, 0.0, -1.0]]),
            translation = np.array([0.35+(position/10), -0.25, 0.01]),
            from_frame = 'franka_tool', to_frame='world')

        fa.goto_pose(des_pose,duration=5.0,use_impedance=False)

        fa.open_gripper()


if __name__ == "__main__":

    fa = FrankaArm()
    fa.reset_joints()

    sw = sandwich_maker()           #instantiate sandwich maker class

    try:
        sw.build_order()
    
    except Exception as e:
        print(e)