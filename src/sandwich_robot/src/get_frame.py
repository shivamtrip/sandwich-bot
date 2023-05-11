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
# from autolab_core import RigidTransform
# from frankapy import FrankaArm


def check_frame(data):

    image = br.imgmsg_to_cv2(data)      # converting from ROS image format to OpenCV image format      

    print("------------------------------------")
    print(" ")

    print(image.shape)
    cv2.imshow("frame", image[:, :, :3])
    cv2.waitKey(1)

    print("Image")
    print(data)




def callback(data):
    # rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
    # time.sleep(1)
    
    image = br.imgmsg_to_cv2(data)      # converting from ROS image format to OpenCV image format   
    image_height = image.shape[0]
    image_width = image.shape[1]    
    # image = image[400:800, 400:1200, :]         # iam-doc
    image = image[200:600, 400:1200, :]         # iam-grumpy
    image_height_ratio = 400 / image_height
    image_width_ratio =  800 / image_width
    print("SIZE: ", image.shape)
    # time.sleep(1)

    print("------------------------------------")
    print(" ")

    # Red Color Bounds
    # lower_red =np.array([161,155,84])         # iam-doc
    # upper_red =np.array([179,255,255])

    lower_red =np.array([161,50,84])            # iam-grumpy
    upper_red =np.array([179,255,255])

    # Yellow Color Bounds
    lower_yellow= np.array([10, 100, 0])
    upper_yellow= np.array([20, 255, 255])


    # image = cv2.resize(image, (800, 600))
    image = image[:, :, :3]         #taking rgb layers of image only

    imgHSV= cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
    red_mask=cv2.inRange(imgHSV,lower_red,upper_red)
    yellow_mask = cv2.inRange(imgHSV,lower_yellow,upper_yellow)

    kernel = np.ones((5, 5), "uint8")
      
    # For red color
    red_mask = cv2.dilate(red_mask, kernel)
    res_red = cv2.bitwise_and(image, image, 
                              mask = red_mask)

    # For yellow color
    yellow_mask = cv2.dilate(yellow_mask, kernel)
    res_yellow = cv2.bitwise_and(image, image, 
                              mask = yellow_mask)


    # im_, contours_red, hierarchy = cv2.findContours(red_mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    # im, contours_yellow, hierarchy = cv2.findContours(yellow_mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    contours_red, hierarchy = cv2.findContours(red_mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    contours_yellow, hierarchy = cv2.findContours(yellow_mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)



    camera_mat = np.array([[75.9609985351562, 0.0, 1018.8323974609375, 0.0, 0.0, 975.6666870117188, 777.054931640625, 0.0, 0.0, 0.0, 1.0, 0.0]])

    intrinsic = np.array([[975.9609985351562, 0.0, 1018.8323974609375], 
                          [0.0, 975.6666870117188, 777.054931640625], 
                          [0.0, 0.0, 1.0]])

    fx = intrinsic[0, 0]
    fy = intrinsic[1, 1]
    cx = intrinsic[0, 2]
    cy = intrinsic[1, 2]

    rotation = np.array([[-0.05437199,  0.99769028, -0.04071191],       # got from camera calibration
                        [0.99807252,  0.05551034,  0.02739719],
                        [0.02959404, -0.03914623, -0.99878567]])

    # translation = np.array([[0.64138432 , 0.1008975 ,  0.831477 ]]).reshape(3, 1)         #iam-doc
    translation = np.array([[0.66138432 , 0.06708975 ,  0.831477 ]]).reshape(3, 1)           # iam-grumpy


    transform = np.hstack((rotation, translation))

    # print("TRANS: ", transform.shape)

    object_x = []               #list storing x coordinates of all objects
    object_y = []               #list storing y coordinates of all objects

    p = Pose()

    for pic, contour in enumerate(contours_red):
        area = cv2.contourArea(contour)
        
        if(area > 5000 and area < 7000):
            print("Red Area: ", area)
            x, y, w, h = cv2.boundingRect(contour)
            image = np.ascontiguousarray(image, dtype=np.uint8)
            image = cv2.rectangle(image, (x, y), 
                                        (x + w, y + h), 
                                        (0, 0, 255), 2)
            us = x + w//2           #center x of object in image frame
            vs = y + h//2           # center y of object in image frame    
            z = 0.83                # depth of object in camera frame    
            cv2.circle(image, (us, vs), 5, 255, 10)

            print("INITIAL PIXELS: ", (us, vs))
            us += 400
            vs += 400

            print("Final: ", (us, vs))

            
            xs = ((us - cx) / fx) * z       # x coordinate of object center in camera frame
            ys = ((vs - cy) / fy) * z       # y coordinate of object center in camera frame

            camera_cord = np.array([[xs, ys, z, 1]]).T

            base_cord = np.matmul(transform, camera_cord).flatten()       # object coordinates in base frame

            if not base_cord[0] < 0.2:
                object_x.append(base_cord[0])
                object_y.append(base_cord[1])

            # p.position.x = base_cord[0]
            # p.position.y = base_cord[1]
            # p.position.z = base_cord[2]
            
            # pub.publish(p)

            print("BASE: ", base_cord)

    bun_x = []
    bun_y = []
    area_list = []

    for pic, contour in enumerate(contours_yellow):
        area = cv2.contourArea(contour)
        
        if(area > 4000):  # and area < 7000):
            print("Yellow Area: ", area)
            x, y, w, h = cv2.boundingRect(contour)
            image = np.ascontiguousarray(image, dtype=np.uint8)
            image = cv2.rectangle(image, (x, y), 
                                        (x + w, y + h), 
                                        (0, 0, 255), 2)
            us = x + w//2           #center x of object in image frame
            vs = y + h//2           # center y of object in image frame    
            z = 0.83                # depth of object in camera frame    
            cv2.circle(image, (us, vs), 5, 255, 10)

            us += 400
            vs += 400
            
            xs = ((us - cx) / fx) * z       # x coordinate of object center in camera frame
            ys = ((vs - cy) / fy) * z       # y coordinate of object center in camera frame

            camera_cord = np.array([[xs, ys, z, 1]]).T

            base_cord = np.matmul(transform, camera_cord).flatten()       # object coordinates in base frame


            bun_x.append(base_cord[0])
            bun_y.append(base_cord[1])
            area_list.append(area)

            print(area, bun_x)

            # p.position.x = base_cord[0]
            # p.position.y = base_cord[1]
            # p.position.z = base_cord[2]
            
            # pub.publish(p)

            # print("BASE: ", base_cord)

    print("AREA SIZE: ", len(area_list))
    try:
        if area_list[0] < area_list[1]:
            print("HERE", bun_x[0])
            object_x.append(bun_x[0])           #appending top bun coordinates first (lesser area)
            object_y.append(bun_y[0])

            object_x.append(bun_x[1])
            object_y.append(bun_y[1])

        else:
            print("THERE")
            object_x.append(bun_x[1])
            object_y.append(bun_y[1])

            object_x.append(bun_x[0])
            object_y.append(bun_y[0])
    except IndexError:
        pass

    
    print("X: ", object_x)
    print("Y: ", object_y)

    pose_pub = object_pose()

    pose_pub.x_pose = object_x
    pose_pub.y_pose = object_y
    pose_pub.num_items = 3

    pub.publish(pose_pub)

    cv2.imshow("mask",yellow_mask)
    cv2.imshow("cam",image)
    cv2.waitKey(1)


def callback_depth(data):

    global depth_image

    depth_image = br.imgmsg_to_cv2(data)      # converting from ROS image format to OpenCV image format      

    cv2.imshow("depth", depth_image)
    cv2.waitKey()

    
def listener():

    rospy.init_node('frame_subscriber', anonymous=True)
    print("HERE")
    # rospy.Subscriber("/rgb/image_raw", Image, callback)         #for iam-doc robot
    rospy.Subscriber("k4a/rgb/image_raw", Image, callback)            # for iam-grumpy robot


    rospy.spin()


if __name__ == '__main__':

    br = CvBridge()
    # pub = rospy.Publisher('goal_pose', Pose, queue_size=1)
    pub = rospy.Publisher('goal_pose', object_pose, queue_size=1)



    listener()