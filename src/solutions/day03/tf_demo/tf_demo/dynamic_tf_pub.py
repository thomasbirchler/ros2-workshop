import rclpy
from rclpy.node import Node
from geometry_msgs.msg import TransformStamped
from tf2_ros.transform_broadcaster import TransformBroadcaster
import math
import time


class DynamicTFPublisher(Node):
    def __init__(self):
        super().__init__('dynamic_tf_pub')
        self.broadcaster = TransformBroadcaster(self)
        self.timer = self.create_timer(0.05, self.timer_callback)  # 20Hz
        self.start_time = time.time()

    def timer_callback(self):
        now = self.get_clock().now().to_msg()
        elapsed = time.time() - self.start_time

        t = TransformStamped()
        t.header.stamp = now
        t.header.frame_id = 'odom'
        t.child_frame_id = 'base_link'

        # Move in a circle
        radius = 1.0
        t.transform.translation.x = radius * math.cos(elapsed)
        t.transform.translation.y = radius * math.sin(elapsed)
        t.transform.translation.z = 0.0
        t.transform.rotation.z = math.sin(elapsed / 2)
        t.transform.rotation.w = math.cos(elapsed / 2)

        self.broadcaster.sendTransform(t)


def main():
    rclpy.init()
    node = DynamicTFPublisher()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == '__main__':
    main()
