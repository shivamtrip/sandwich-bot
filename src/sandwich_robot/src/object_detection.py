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
from collections import defaultdict

"""
This script takes as input camera feed and outputs an array 
containing image coordinates of every object in frame
"""
#Test
class ColorDetector:

    def _init_(self):

        self.image = None

        self.number_of_colors = 2
        self.contours = []

        # Red Color Bounds
        self.lower_red =np.array([161,155,84])         # iam-doc
        self.upper_red =np.array([179,255,255])

        # Yellow Color Bounds
        self.lower_yellow= np.array([10, 100, 0])
        self.upper_yellow= np.array([20, 255, 255])

        self.kernel = np.ones((5, 5), "uint8")

        self.object_centers = defaultdict(list)
    
    def read_image(self, data):
        self.image = br.imgmsg_to_cv2(data)      # converting from ROS image format to OpenCV image format  
        self.image = self.image[:, :, :3]         #taking rgb layers of image only 
        self.crop_image()                 

    def crop_image(self):
        self.image = self.image[400:800, 400:1200, :]

    def get_mask(self):
        
        self.imgHSV= cv2.cvtColor(self.image,cv2.COLOR_BGR2HSV)
        self.red_mask=cv2.inRange(self.imgHSV,self.lower_red,self.upper_red)
        self.yellow_mask = cv2.inRange(self.imgHSV,self.lower_yellow,self.upper_yellow)
     
        # For red color
        self.red_mask = cv2.dilate(self.red_mask, self.kernel)
        self.res_red = cv2.bitwise_and(self.image, self.image, 
                                mask = self.red_mask)

        # For yellow color
        self.yellow_mask = cv2.dilate(self.yellow_mask, self.kernel)
        self.res_yellow = cv2.bitwise_and(self.image, self.image, 
                                mask = self.yellow_mask)

    def get_contours(self):
        im_, self.contours_red, hierarchy = cv2.findContours(self.red_mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        im, self.contours_yellow, hierarchy = cv2.findContours(self.yellow_mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

        self.contours = [self.contours_red, self.contours_yellow]

        for i in range(self.number_of_colors):
            cur_contour = self.contours[i]

            for pic, contour in enumerate(cur_contour):
                area = cv2.contourArea(contour)
                
                if(area > 4000):
                    x, y, w, h = cv2.boundingRect(contour)
                    self.image = np.ascontiguousarray(self.image, dtype=np.uint8)
                    self.image = cv2.rectangle(self.image, (x, y), 
                                                (x + w, y + h), 
                                                (0, 0, 255), 2)
                    us = x + w//2           #center x of object in image frame
                    vs = y + h//2           # center y of object in image frame    
                    z = 0.83                # depth of object in camera frame    
                    cv2.circle(self.image, (us, vs), 5, 255, 10)

                    us += 400
                    vs += 400

                if i == 1:
                    self.object_centers["red"].append((us, vs))
                elif i == 2:
                    self.object_centers["yellow"].append((us, vs))

                    if len(self.object_centers["yellow"]) == 2:
                        self.yellow_area2 = area
                    else:
                        self.yellow_area1 = area

    def create_image_message(self):
        self.object_center_x = []
        self.object_center_y = []

        # Append coordinates of tomato (red ingredient)
        self.object_center_x.append(self.object_centers["red"][0][0])
        self.object_center_y.append(self.object_centers["red"][0][1])

        # Append coordinates of bun (yellow ingredient)
        if self.yellow_area1 < self.yellow_area2:
            self.object_center_x.append(self.object_centers["yellow"][0][0])
            self.object_center_y.append(self.object_centers["yellow"][0][1])

            self.object_center_x.append(self.object_centers["yellow"][1][0])
            self.object_center_y.append(self.object_centers["yellow"][1][1])

        else:
            self.object_center_x.append(self.object_centers["yellow"][1][0])
            self.object_center_y.append(self.object_centers["yellow"][1][1])

            self.object_center_x.append(self.object_centers["yellow"][0][0])
            self.object_center_y.append(self.object_centers["yellow"][0][1])
    
    def send_image_coordinates(self):
        self.pose_pub = object_centers()

        self.pose_pub.x_pose = self.object_center_x
        self.pose_pub.y_pose = self.object_center_y
        self.pose_pub.num_items = 3

        pub.publish(self.pose_pub)

    def start_listener(self):
        rospy.Subscriber("/rgb/image_raw", Image, self.read_image)         #for iam-doc robot

    def main(self):

        rospy.init_node('object_detector', anonymous=True)

        self.start_listener()

        if self.image:
            self.get_mask()
            self.get_contours()
            self.create_image_message()
            self.send_image_coordinates()

        rospy.spin()


if __name__ == "__main__":

    br = CvBridge()
    pub = rospy.Publisher('object_center_publisher', object_centers, queue_size=1)

    detector = ColorDetector()

    detector.main()


