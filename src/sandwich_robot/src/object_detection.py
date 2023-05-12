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
from sandwich_robot.msg import object_pose

"""
This script takes as input camera feed and outputs an array 
containing image coordinates of every object in frame
"""

class ColorDetector:

    def _init_(self):
        return

    def crop_image(self, img):
        return
    
    def get_contours(self, img):

    def compare_area(self, img):

    def send_image_coordinates(self, image):


if __name__ == "__main__":

    detector = ColorDetector()
    

