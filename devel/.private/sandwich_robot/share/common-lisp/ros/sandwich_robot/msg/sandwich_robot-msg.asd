
(cl:in-package :asdf)

(defsystem "sandwich_robot-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :std_msgs-msg
)
  :components ((:file "_package")
    (:file "object_centers" :depends-on ("_package_object_centers"))
    (:file "_package_object_centers" :depends-on ("_package"))
    (:file "object_pose" :depends-on ("_package_object_pose"))
    (:file "_package_object_pose" :depends-on ("_package"))
  ))