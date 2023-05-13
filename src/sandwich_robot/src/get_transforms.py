#!/usr/bin/env python
from email.mime import base
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
import os
import numpy as np
import time
from geometry_msgs.msg import Pose
from sandwich_robot.msg import object_centers
from sandwich_robot.msg import object_pose
from collections import defaultdict

class Transform_Coordinates:

    def _init_(self):

        self.camera_intrinsics = np.array([[975.9609985351562, 0.0, 1018.8323974609375], 
                            [0.0, 975.6666870117188, 777.054931640625], 
                            [0.0, 0.0, 1.0]])

        self.fx = self.camera_intrinsics[0, 0]
        self.fy = self.camera_intrinsics[1, 1]
        self.cx = self.camera_intrinsics[0, 2]
        self.cy = self.camera_intrinsics[1, 2]

        self.z = 0.83                # depth of object in camera frame 

        self.rotation = np.array([[-0.05437199,  0.99769028, -0.04071191],       # got from camera calibration
                            [0.99807252,  0.05551034,  0.02739719],
                            [0.02959404, -0.03914623, -0.99878567]])

        self.translation = np.array([[0.64138432 , 0.1208975 ,  0.831477 ]]).reshape(3, 1)         #iam-doc

        self.camera_to_base_transform = np.hstack((self.rotation, self.translation))

        self.object_x = []               #list storing x coordinates of all objects
        self.object_y = []               #list storing y coordinates of all objects

    def start_listener(self):
        rospy.Subscriber("/object_center_publisher", object_centers, self.transform)         #for iam-doc robot

    def transform(self, data):
        for i in range(data.num_items):
            xs = ((data.x_center[i] - self.cx) / self.fx) * self.z       # x coordinate of object center in camera frame
            ys = ((data.y_center[i] - self.cy) / self.fy) * self.z       # y coordinate of object center in camera frame

            camera_cord = np.array([[xs, ys, self.z, 1]]).T

            base_cord = np.matmul(self.camera_to_base_transform, camera_cord).flatten()       # object coordinates in base frame

            # if not base_cord[0] < 0.2:
            self.object_x.append(base_cord[0])
            self.object_y.append(base_cord[1])
        
        self.publish_transforms()

    def publish_transforms(self):

        pose_pub = object_pose()

        pose_pub.x_pose = self.object_x
        pose_pub.y_pose = self.object_y
        pose_pub.num_items = 3

        pub.publish(pose_pub)

    def main(self):

        rospy.init_node('coordinate_transformer', anonymous=True)
        self.start_listener()

        rospy.spin()
        


if __name__ == "__main__":

    transformer = Transform_Coordinates()
    pub = rospy.Publisher('object_transform_publisher', object_pose, queue_size=1)

    transformer.main()

