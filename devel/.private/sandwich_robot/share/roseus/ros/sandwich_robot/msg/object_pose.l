;; Auto-generated. Do not edit!


(when (boundp 'sandwich_robot::object_pose)
  (if (not (find-package "SANDWICH_ROBOT"))
    (make-package "SANDWICH_ROBOT"))
  (shadow 'object_pose (find-package "SANDWICH_ROBOT")))
(unless (find-package "SANDWICH_ROBOT::OBJECT_POSE")
  (make-package "SANDWICH_ROBOT::OBJECT_POSE"))

(in-package "ROS")
;;//! \htmlinclude object_pose.msg.html
(if (not (find-package "STD_MSGS"))
  (ros::roseus-add-msgs "std_msgs"))


(defclass sandwich_robot::object_pose
  :super ros::object
  :slots (_header _x_pose _y_pose _num_items ))

(defmethod sandwich_robot::object_pose
  (:init
   (&key
    ((:header __header) (instance std_msgs::Header :init))
    ((:x_pose __x_pose) (make-array 0 :initial-element 0.0 :element-type :float))
    ((:y_pose __y_pose) (make-array 0 :initial-element 0.0 :element-type :float))
    ((:num_items __num_items) 0.0)
    )
   (send-super :init)
   (setq _header __header)
   (setq _x_pose __x_pose)
   (setq _y_pose __y_pose)
   (setq _num_items (float __num_items))
   self)
  (:header
   (&rest __header)
   (if (keywordp (car __header))
       (send* _header __header)
     (progn
       (if __header (setq _header (car __header)))
       _header)))
  (:x_pose
   (&optional __x_pose)
   (if __x_pose (setq _x_pose __x_pose)) _x_pose)
  (:y_pose
   (&optional __y_pose)
   (if __y_pose (setq _y_pose __y_pose)) _y_pose)
  (:num_items
   (&optional __num_items)
   (if __num_items (setq _num_items __num_items)) _num_items)
  (:serialization-length
   ()
   (+
    ;; std_msgs/Header _header
    (send _header :serialization-length)
    ;; float32[] _x_pose
    (* 4    (length _x_pose)) 4
    ;; float32[] _y_pose
    (* 4    (length _y_pose)) 4
    ;; float32 _num_items
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; std_msgs/Header _header
       (send _header :serialize s)
     ;; float32[] _x_pose
     (write-long (length _x_pose) s)
     (dotimes (i (length _x_pose))
       (sys::poke (elt _x_pose i) (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
       )
     ;; float32[] _y_pose
     (write-long (length _y_pose) s)
     (dotimes (i (length _y_pose))
       (sys::poke (elt _y_pose i) (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
       )
     ;; float32 _num_items
       (sys::poke _num_items (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; std_msgs/Header _header
     (send _header :deserialize buf ptr-) (incf ptr- (send _header :serialization-length))
   ;; float32[] _x_pose
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _x_pose (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _x_pose i) (sys::peek buf ptr- :float)) (incf ptr- 4)
     ))
   ;; float32[] _y_pose
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _y_pose (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _y_pose i) (sys::peek buf ptr- :float)) (incf ptr- 4)
     ))
   ;; float32 _num_items
     (setq _num_items (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get sandwich_robot::object_pose :md5sum-) "ca7e8735ece8702de0499ffa6d63bc95")
(setf (get sandwich_robot::object_pose :datatype-) "sandwich_robot/object_pose")
(setf (get sandwich_robot::object_pose :definition-)
      "Header header
float32[] x_pose
float32[] y_pose
float32 num_items
================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
string frame_id

")



(provide :sandwich_robot/object_pose "ca7e8735ece8702de0499ffa6d63bc95")


