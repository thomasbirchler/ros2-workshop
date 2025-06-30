import rclpy
from rclpy.node import Node

import math
import time


class DynamicTFPublisher(Node):
    def __init__(self):
        # Add a unique name for the node (e.g. 'dynamic_tf_pub')
        super().__init__('node_name')
        # Add the following import to the beginning of the file: from tf2_ros.transform_broadcaster import TransformBroadcaster
        # Create a TransformBroadcaster(self) instance
        self.broadcaster = 
        # Create a timer with a 50ms period (20Hz) to call the timer_callback method: self.create_timer(time_period, function_to_call)
        self.timer = 
        self.start_time = time.time()

    def timer_callback(self):
        now = self.get_clock().now().to_msg()
        elapsed = time.time() - self.start_time

        # Add the following to beginning of the file: from geometry_msgs.msg import TransformStamped
        # Create a TransformStamped() message
        t = 
        t.header.stamp = now
        # Add the the parent frame_id: 'odom'
        t.header.frame_id 
        # Add the child frame_id: 'base_link'
        t.child_frame_id =

        # Move in a circle
        radius = 1.0
        t.transform.translation.x = radius * math.cos(elapsed)
        t.transform.translation.y = radius * math.sin(elapsed)
        t.transform.translation.z = 0.0
        t.transform.rotation.z = math.sin(elapsed / 2)
        t.transform.rotation.w = math.cos(elapsed / 2)

        # Use the broadcaster to send the transform: self.broadcaster.sendTransform(t)
        self.


def main():
    rclpy.init()
    # Create an instance of the DynamicTFPublisher class
    node = 
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == '__main__':
    main()
