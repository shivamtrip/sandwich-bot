; Auto-generated. Do not edit!


(cl:in-package sandwich_robot-msg)


;//! \htmlinclude object_pose.msg.html

(cl:defclass <object_pose> (roslisp-msg-protocol:ros-message)
  ((header
    :reader header
    :initarg :header
    :type std_msgs-msg:Header
    :initform (cl:make-instance 'std_msgs-msg:Header))
   (x_pose
    :reader x_pose
    :initarg :x_pose
    :type (cl:vector cl:float)
   :initform (cl:make-array 0 :element-type 'cl:float :initial-element 0.0))
   (y_pose
    :reader y_pose
    :initarg :y_pose
    :type (cl:vector cl:float)
   :initform (cl:make-array 0 :element-type 'cl:float :initial-element 0.0))
   (num_items
    :reader num_items
    :initarg :num_items
    :type cl:float
    :initform 0.0))
)

(cl:defclass object_pose (<object_pose>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <object_pose>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'object_pose)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name sandwich_robot-msg:<object_pose> is deprecated: use sandwich_robot-msg:object_pose instead.")))

(cl:ensure-generic-function 'header-val :lambda-list '(m))
(cl:defmethod header-val ((m <object_pose>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader sandwich_robot-msg:header-val is deprecated.  Use sandwich_robot-msg:header instead.")
  (header m))

(cl:ensure-generic-function 'x_pose-val :lambda-list '(m))
(cl:defmethod x_pose-val ((m <object_pose>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader sandwich_robot-msg:x_pose-val is deprecated.  Use sandwich_robot-msg:x_pose instead.")
  (x_pose m))

(cl:ensure-generic-function 'y_pose-val :lambda-list '(m))
(cl:defmethod y_pose-val ((m <object_pose>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader sandwich_robot-msg:y_pose-val is deprecated.  Use sandwich_robot-msg:y_pose instead.")
  (y_pose m))

(cl:ensure-generic-function 'num_items-val :lambda-list '(m))
(cl:defmethod num_items-val ((m <object_pose>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader sandwich_robot-msg:num_items-val is deprecated.  Use sandwich_robot-msg:num_items instead.")
  (num_items m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <object_pose>) ostream)
  "Serializes a message object of type '<object_pose>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'header) ostream)
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'x_pose))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let ((bits (roslisp-utils:encode-single-float-bits ele)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)))
   (cl:slot-value msg 'x_pose))
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'y_pose))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let ((bits (roslisp-utils:encode-single-float-bits ele)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)))
   (cl:slot-value msg 'y_pose))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'num_items))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <object_pose>) istream)
  "Deserializes a message object of type '<object_pose>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'header) istream)
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'x_pose) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'x_pose)))
    (cl:dotimes (i __ros_arr_len)
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:aref vals i) (roslisp-utils:decode-single-float-bits bits))))))
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'y_pose) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'y_pose)))
    (cl:dotimes (i __ros_arr_len)
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:aref vals i) (roslisp-utils:decode-single-float-bits bits))))))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'num_items) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<object_pose>)))
  "Returns string type for a message object of type '<object_pose>"
  "sandwich_robot/object_pose")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'object_pose)))
  "Returns string type for a message object of type 'object_pose"
  "sandwich_robot/object_pose")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<object_pose>)))
  "Returns md5sum for a message object of type '<object_pose>"
  "ca7e8735ece8702de0499ffa6d63bc95")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'object_pose)))
  "Returns md5sum for a message object of type 'object_pose"
  "ca7e8735ece8702de0499ffa6d63bc95")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<object_pose>)))
  "Returns full string definition for message of type '<object_pose>"
  (cl:format cl:nil "Header header~%float32[] x_pose~%float32[] y_pose~%float32 num_items~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'object_pose)))
  "Returns full string definition for message of type 'object_pose"
  (cl:format cl:nil "Header header~%float32[] x_pose~%float32[] y_pose~%float32 num_items~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <object_pose>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'header))
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'x_pose) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 4)))
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'y_pose) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 4)))
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <object_pose>))
  "Converts a ROS message object to a list"
  (cl:list 'object_pose
    (cl:cons ':header (header msg))
    (cl:cons ':x_pose (x_pose msg))
    (cl:cons ':y_pose (y_pose msg))
    (cl:cons ':num_items (num_items msg))
))
