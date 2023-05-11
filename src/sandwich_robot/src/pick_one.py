import numpy as np
from autolab_core import RigidTransform
from frankapy import FrankaArm
import rospy
from geometry_msgs.msg import Pose
import time
from sandwich_robot.msg import object_pose


class sandwich_maker:
    def __init__(self):
        fa = FrankaArm()
        fa.reset_joints()
        # rospy.Subscriber("/goal_pose", Pose, self.callback)
        rospy.Subscriber("/goal_pose", object_pose, self.callback)


        self.des_x = None
        self.des_y = None


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

        # print(self.des_x)


    def pick_object(self,position):

        if self.tomato_pos: # and self.des_y:
            # print(self.des_x, self.des_y)

            fa.open_gripper()
            cur_x = self.tomato_pos[0]
            cur_y = self.tomato_pos[1]

            print("HERE")
            des_pose = RigidTransform(rotation=np.array([
            [1.0, 0.0, 0.0],
            [0.0, -1.0, 0.0],
            [0.0, 0.0, -1.0]]),
            # translation = np.array([0.35+(position/10), -0.25, 0.009]),
            translation = np.array([cur_x, cur_y, 0.02]),
            from_frame = 'franka_tool', to_frame='world')

            fa.goto_pose(des_pose,duration=5.0,use_impedance=False)

            print("HERE")
            des_pose = RigidTransform(rotation=np.array([
            [1.0, 0.0, 0.0],
            [0.0, -1.0, 0.0],
            [0.0, 0.0, -1.0]]),
            # translation = np.array([0.35+(position/10), -0.25, 0.009]),
            translation = np.array([cur_x, cur_y, 0.006]),
            from_frame = 'franka_tool', to_frame='world')

            fa.goto_pose(des_pose,duration=1.0,use_impedance=False)

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
        number_of_items = 1             
        time.sleep(1)

        while not rospy.is_shutdown():
            print("Making your sandwich")
            for i in range(number_of_items):
        
                self.pick_object(i)
                self.reset_pose()              
                self.place_object(i-0.1)
                self.reset_pose()


    

if __name__ == "__main__":

    fa = FrankaArm()
    fa.reset_joints()

    sw = sandwich_maker()           #instantiate sandwich maker class

    try:
        sw.build_order()
    
    except Exception as e:
        print(e)