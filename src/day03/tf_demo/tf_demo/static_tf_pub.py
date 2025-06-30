import rclpy
from rclpy.node import Node


class StaticTFPublisher(Node):
    def __init__(self):
        # Add a unique name for the node (e.g. 'static_tf_pub')
        super().__init__('node_name')
        # Add the following import to the beginning of the file: from tf2_ros.static_transform_broadcaster import StaticTransformBroadcaster
        # Create a StaticTransformBroadcaster(self) instance
        broadcaster = 

        # Add the following import to the beginning of the file: from geometry_msgs.msg import TransformStamped
        # Create a TransformStamped() message
        t = 
        t.header.stamp = self.get_clock().now().to_msg()
        # Add the the parent frame_id: 'base_link'
        t.header.frame_id = 
        # Add the child frame_id: 'camera_link'
        t.child_frame_id = 
        # Move the camera 0.5m in x direction of the robot, 0.0m in y direction and 0.2m in z direction.
        t.transform.translation.x = 
        t.transform.translation.y = 
        t.transform.translation.z = 
        t.transform.rotation.w = 1.0  # no rotation

        # Use the broadcaster to send the transform: broadcaster.sendTransform(t)
        broadcaster.


def main():
    rclpy.init()
    # Create an instance of the StaticTFPublisher class
    node = 
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == '__main__':
    main()
