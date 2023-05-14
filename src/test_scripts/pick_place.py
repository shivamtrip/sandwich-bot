import numpy as np

from autolab_core import RigidTransform
from frankapy import FrankaArm


def move_arm():
    fa.goto_joints([0.0,-0.7,0.0,-2.15,0.0,1.57,0.7])

    fa.close_gripper()
    fa.open_gripper()
    

def move_endeffector(position):
    if position == 1:
        des_pose = RigidTransform(rotation=np.array([
        [1.0, 0.0, 0.0],
        [0.0, -1.0, 0.0],
        [0.0, 0.0, -1.0]]),
        translation = np.array([0.35+(position/10), -0.25, 0.009]),
        from_frame = 'franka_tool', to_frame='world')
    else:
        des_pose = RigidTransform(rotation=np.array([
            [1.0, 0.0, 0.0],
            [0.0, -1.0, 0.0],
            [0.0, 0.0, -1.0]]),
            translation = np.array([0.35+(position/10), -0.25, 0.01]),
            from_frame = 'franka_tool', to_frame='world')

    fa.goto_pose(des_pose,duration=5.0,use_impedance=False)
    

def def_pose():
    
    des_pose = RigidTransform(rotation=np.array([
        [1.0, 0.0, 0.0],
        [0.0, -1.0, 0.0],
        [0.0, 0.0, -1.0]]),
        translation = np.array([0.35, 0.0, 0.35]),
        from_frame = 'franka_tool', to_frame='world')

    fa.goto_pose(des_pose,duration=5.0, use_impedance=False)


    
def place_box(box_number):
    # print("Item number:" + str(box_number+1))
    des_pose = RigidTransform(rotation=np.array([
        [1.0, 0.0, 0.0],
        [0.0, -1.0, 0.0],
        [0.0, 0.0, -1.0]]),
        translation = np.array([0.35, 0, (0.012*(box_number+1)+0.015)]),
        from_frame = 'franka_tool', to_frame='world')

    fa.goto_pose(des_pose,duration = 5.0, use_impedance=False)

def place_hot_dog(item_number):
    # print("Item number:" + str(box_number+1))
    des_pose = RigidTransform(rotation=np.array([
        [1.0, 0.0, 0.0],
        [0.0, -1.0, 0.0],
        [0.0, 0.0, -1.0]]),
        translation = np.array([0.35, -0.1, (0.012 + (item_number*2)*0.015)]),
        from_frame = 'franka_tool', to_frame='world')

    fa.goto_pose(des_pose,duration = 5.0, use_impedance=False)

def grab_hotdog(item_number):
    # print("Item number:" + str(box_number+1))
    des_pose = RigidTransform(rotation=np.array([
        [1.0, 0.0, 0.0],
        [0.0, -1.0, 0.0],
        [0.0, 0.0, -1.0]]),
        translation = np.array([0.55, 0+(item_number/10), 0.012]),
        from_frame = 'franka_tool', to_frame='world')

    fa.goto_pose(des_pose,duration = 5.0, use_impedance=False)    

if __name__ == "__main__":
    fa = FrankaArm()
    fa.reset_joints()
    box_number = 3

    # End effector pose 
    T__ee_world = fa.get_pose()
    # print('translation:  {}'.format(T__ee_world.translation))
    # print('Rotation: {}'.format(T__ee_world.quaternion))

    # joint angles
    joints = fa.get_joints()
    # print('Joints: {}'.format(joints))

    #Gripper width
    gripper_width = fa.get_gripper_width()
    # print('Gripper width: {}'.format(gripper_width))

    #End effector forces 
    force_torque = fa.get_ee_force_torque()
    # print('Forces and torques: {}'.format(force_torque))
    
    while(1):
        print("Making your sandwich")
        for i in range(box_number):
        # move_arm()
        
            move_endeffector(i)
            fa.close_gripper()
            def_pose()
            place_box(i-0.1)
            fa.open_gripper()
            def_pose()
        
        print("Making your hotdog")
        
        for i in range(2):
            grab_hotdog(i)
            fa.close_gripper()
            def_pose()
            place_hot_dog(i)
            fa.open_gripper()
            def_pose()


        print("Your order is ready")

        print("cancelling order")
        for i in range(box_number-1,-1,-1):
        # move_arm()
    
            place_box(i-1.5)
            fa.close_gripper()
            def_pose()
            move_endeffector(i)
            fa.open_gripper()        
            def_pose()

       

    #Function
