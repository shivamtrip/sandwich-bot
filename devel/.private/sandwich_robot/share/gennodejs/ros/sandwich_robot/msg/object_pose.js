// Auto-generated. Do not edit!

// (in-package sandwich_robot.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let std_msgs = _finder('std_msgs');

//-----------------------------------------------------------

class object_pose {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.header = null;
      this.x_pose = null;
      this.y_pose = null;
      this.num_items = null;
    }
    else {
      if (initObj.hasOwnProperty('header')) {
        this.header = initObj.header
      }
      else {
        this.header = new std_msgs.msg.Header();
      }
      if (initObj.hasOwnProperty('x_pose')) {
        this.x_pose = initObj.x_pose
      }
      else {
        this.x_pose = [];
      }
      if (initObj.hasOwnProperty('y_pose')) {
        this.y_pose = initObj.y_pose
      }
      else {
        this.y_pose = [];
      }
      if (initObj.hasOwnProperty('num_items')) {
        this.num_items = initObj.num_items
      }
      else {
        this.num_items = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type object_pose
    // Serialize message field [header]
    bufferOffset = std_msgs.msg.Header.serialize(obj.header, buffer, bufferOffset);
    // Serialize message field [x_pose]
    bufferOffset = _arraySerializer.float32(obj.x_pose, buffer, bufferOffset, null);
    // Serialize message field [y_pose]
    bufferOffset = _arraySerializer.float32(obj.y_pose, buffer, bufferOffset, null);
    // Serialize message field [num_items]
    bufferOffset = _serializer.float32(obj.num_items, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type object_pose
    let len;
    let data = new object_pose(null);
    // Deserialize message field [header]
    data.header = std_msgs.msg.Header.deserialize(buffer, bufferOffset);
    // Deserialize message field [x_pose]
    data.x_pose = _arrayDeserializer.float32(buffer, bufferOffset, null)
    // Deserialize message field [y_pose]
    data.y_pose = _arrayDeserializer.float32(buffer, bufferOffset, null)
    // Deserialize message field [num_items]
    data.num_items = _deserializer.float32(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += std_msgs.msg.Header.getMessageSize(object.header);
    length += 4 * object.x_pose.length;
    length += 4 * object.y_pose.length;
    return length + 12;
  }

  static datatype() {
    // Returns string type for a message object
    return 'sandwich_robot/object_pose';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'ca7e8735ece8702de0499ffa6d63bc95';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    Header header
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
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new object_pose(null);
    if (msg.header !== undefined) {
      resolved.header = std_msgs.msg.Header.Resolve(msg.header)
    }
    else {
      resolved.header = new std_msgs.msg.Header()
    }

    if (msg.x_pose !== undefined) {
      resolved.x_pose = msg.x_pose;
    }
    else {
      resolved.x_pose = []
    }

    if (msg.y_pose !== undefined) {
      resolved.y_pose = msg.y_pose;
    }
    else {
      resolved.y_pose = []
    }

    if (msg.num_items !== undefined) {
      resolved.num_items = msg.num_items;
    }
    else {
      resolved.num_items = 0.0
    }

    return resolved;
    }
};

module.exports = object_pose;
