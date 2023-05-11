
import numpy as np
from autolab_core import RigidTransform
from frankapy import FrankaArm 
import rospy
from geometry_msgs.msg import Pose

if __name__ == "__main__":
    fa = FrankaArm()

    # fa.reset_joints()
    # fa.open_gripper()
    # fa.close_gripper()

    print("Starting Guide Mode")
    # fa.run_guide_mode(30)
    print("End Guide Mode")

    robot_pose = fa.get_pose()

    # print("Pose: ", robot_pose)

    offset_pose = RigidTransform(translation = np.array([0.0425, 0, -0.01]),
                            rotation = np.array([[0, 0, 1], [-1, 0, 0], [0, -1, 0]]),
                            from_frame = "aruco_pose", to_frame = "franka_tool")

    aruco_pose = rospy.wait_for_message("/aruco_simple/pose", Pose, timeout=5)
    aruco_rt_pose = RigidTransform.from_pose_msg(aruco_pose, from_frame="aruco_pose",
                        to_frame="camera")

    camera_offset = robot_pose * offset_pose * aruco_rt_pose.inverse()      # wrt robot base

    print("Camera Offset")
    print(camera_offset)

    aruco_global = camera_offset * aruco_rt_pose   # estimated aruco pose 

    print("Actual: ", robot_pose)    
    print("Estimate: ", aruco_global)

    camera_offset.save("camera_cal.tf")


