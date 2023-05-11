from asyncio import base_tasks
import numpy as np
from autolab_core import RigidTransform
from frankapy import FrankaArm 
import rospy
from geometry_msgs.msg import Pose



if __name__ == "__main__":
    fa = FrankaArm()
    fa.reset_joints()
    # fa.open_gripper()

    aruco_pose = rospy.wait_for_message("/aruco_simple/pose", Pose, timeout=5)
    # print(aruco_pose)
    aruco_rt_pose = RigidTransform.from_pose_msg(aruco_pose, from_frame="aruco_pose",
                        to_frame="camera")

    print(aruco_rt_pose)

    # camera_offset = RigidTransform(translation = np.array([0.61138432, 0.0908975,  0.831477 ]), 
    #                         rotation = np.array([[-0.05437199,  0.99769028, -0.04071191],
    #                                     [ 0.99807252,  0.05551034,  0.02739719],
    #                                     [ 0.02959404, -0.03914623, -0.99878567]]),
    #                         from_frame = 'camera', to_frame = 'world')

    base_to_camera = RigidTransform.load("camera_cal.tf")
    print("BASE TO CAMERA: ", base_to_camera)

    aruco_global = base_to_camera * aruco_rt_pose   # estimated aruco pose 

    print(aruco_global)

    # aruco_global.translation

    # print("Translation: ")
    # print(cur_translation)
    # aruco_global.tra = np.array()

    des_pose = RigidTransform(rotation = np.array([
        [1, 0, 0],
        [0, -1, 0],
        [0, 0, -1]]),
        translation = aruco_global.translation,
        from_frame ='franka_tool', to_frame ='world')

    fa.goto_pose(des_pose, use_impedance = False, duration = 10)


    # print(des_pose)