from autolab_core import RigidTransform
from frankapy import FrankaArm
import numpy as np
from geometry_msgs.msg import Pose
import rospy


def update_goal(pose):

    global stop_moving
    global des_x
    global des_y


    des_x = pose.position.x
    des_y = pose.position.y

    if not stop_moving:
        pick()
        stop_moving = True

    # print(des_x, des_y)



def pick():

    global stop_moving
    global des_x
    global des_y

    print("MOVING")

    fa.open_gripper()

    des_pose = RigidTransform(rotation=np.array([
    [1.0, 0.0, 0.0],
    [0.0, -1.0, 0.0],
    [0.0, 0.0, -1.0]]),
    translation = np.array([des_x, des_y, 0.007]),
    from_frame = 'franka_tool', to_frame='world')

    if not stop_moving:
        print(des_x, des_y)
        fa.goto_pose(des_pose,duration=5.0,use_impedance=False)
        stop_moving = True

    fa.close_gripper()
    def_pose()

    
def def_pose():
    
    des_pose = RigidTransform(rotation=np.array([
        [1.0, 0.0, 0.0],
        [0.0, -1.0, 0.0],
        [0.0, 0.0, -1.0]]),
        translation = np.array([0.35, 0.0, 0.35]),
        from_frame = 'franka_tool', to_frame='world')

    fa.goto_pose(des_pose,duration=5.0, use_impedance=False)

    place_box(0)



def place_box(box_number):
    # print("Item number:" + str(box_number+1))
    des_pose = RigidTransform(rotation=np.array([
        [1.0, 0.0, 0.0],
        [0.0, -1.0, 0.0],
        [0.0, 0.0, -1.0]]),
        translation = np.array([0.35, 0, (0.012*(box_number+1)+0.015)]),
        from_frame = 'franka_tool', to_frame='world')

    fa.goto_pose(des_pose,duration = 5.0, use_impedance=False)

    fa.open_gripper()




if __name__ == "__main__":

    fa = FrankaArm()
    fa.reset_joints()
    fa.open_gripper()

    # rospy.init_node('move_robot', anonymous=True)

    stop_moving = False
    des_x = None
    des_y = None

    print("TEST")
    rospy.Subscriber("/goal_pose", Pose, update_goal)

    # if des_x and des_y:
    #     pick()

    rospy.spin()

    # move_robot(0,0, 0)
