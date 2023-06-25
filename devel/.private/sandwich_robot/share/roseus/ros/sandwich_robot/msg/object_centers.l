;; Auto-generated. Do not edit!


(when (boundp 'sandwich_robot::object_centers)
  (if (not (find-package "SANDWICH_ROBOT"))
    (make-package "SANDWICH_ROBOT"))
  (shadow 'object_centers (find-package "SANDWICH_ROBOT")))
(unless (find-package "SANDWICH_ROBOT::OBJECT_CENTERS")
  (make-package "SANDWICH_ROBOT::OBJECT_CENTERS"))

(in-package "ROS")
;;//! \htmlinclude object_centers.msg.html
(if (not (find-package "STD_MSGS"))
  (ros::roseus-add-msgs "std_msgs"))


(defclass sandwich_robot::object_centers
  :super ros::object
  :slots (_header _x_center _y_center _num_items _status ))

(defmethod sandwich_robot::object_centers
  (:init
   (&key
    ((:header __header) (instance std_msgs::Header :init))
    ((:x_center __x_center) (make-array 0 :initial-element 0.0 :element-type :float))
    ((:y_center __y_center) (make-array 0 :initial-element 0.0 :element-type :float))
    ((:num_items __num_items) 0)
    ((:status __status) nil)
    )
   (send-super :init)
   (setq _header __header)
   (setq _x_center __x_center)
   (setq _y_center __y_center)
   (setq _num_items (round __num_items))
   (setq _status __status)
   self)
  (:header
   (&rest __header)
   (if (keywordp (car __header))
       (send* _header __header)
     (progn
       (if __header (setq _header (car __header)))
       _header)))
  (:x_center
   (&optional __x_center)
   (if __x_center (setq _x_center __x_center)) _x_center)
  (:y_center
   (&optional __y_center)
   (if __y_center (setq _y_center __y_center)) _y_center)
  (:num_items
   (&optional __num_items)
   (if __num_items (setq _num_items __num_items)) _num_items)
  (:status
   (&optional __status)
   (if __status (setq _status __status)) _status)
  (:serialization-length
   ()
   (+
    ;; std_msgs/Header _header
    (send _header :serialization-length)
    ;; float32[] _x_center
    (* 4    (length _x_center)) 4
    ;; float32[] _y_center
    (* 4    (length _y_center)) 4
    ;; int32 _num_items
    4
    ;; bool _status
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; std_msgs/Header _header
       (send _header :serialize s)
     ;; float32[] _x_center
     (write-long (length _x_center) s)
     (dotimes (i (length _x_center))
       (sys::poke (elt _x_center i) (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
       )
     ;; float32[] _y_center
     (write-long (length _y_center) s)
     (dotimes (i (length _y_center))
       (sys::poke (elt _y_center i) (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
       )
     ;; int32 _num_items
       (write-long _num_items s)
     ;; bool _status
       (if _status (write-byte -1 s) (write-byte 0 s))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; std_msgs/Header _header
     (send _header :deserialize buf ptr-) (incf ptr- (send _header :serialization-length))
   ;; float32[] _x_center
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _x_center (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _x_center i) (sys::peek buf ptr- :float)) (incf ptr- 4)
     ))
   ;; float32[] _y_center
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _y_center (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _y_center i) (sys::peek buf ptr- :float)) (incf ptr- 4)
     ))
   ;; int32 _num_items
     (setq _num_items (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; bool _status
     (setq _status (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;;
   self)
  )

(setf (get sandwich_robot::object_centers :md5sum-) "d43144be60cdeb0179fa3adfa2875f25")
(setf (get sandwich_robot::object_centers :datatype-) "sandwich_robot/object_centers")
(setf (get sandwich_robot::object_centers :definition-)
      "Header header
float32[] x_center
float32[] y_center
int32 num_items
bool status
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



(provide :sandwich_robot/object_centers "d43144be60cdeb0179fa3adfa2875f25")


