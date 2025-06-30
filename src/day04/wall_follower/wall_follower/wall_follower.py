import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist
import numpy as np

class WallFollower(Node):
    def __init__(self):
        super().__init__('wall_follower')
        self.cmd_pub = self.create_publisher(Twist, '/cmd_vel', 10)
        self.scan_sub = self.create_subscription(LaserScan, '/scan', self.scan_callback, 10)
        self.timer = self.create_timer(0.1, self.control_loop)

        self.right_distance = 0.0
        self.front_distance = 0.0
        self.target_distance = 0.5  # desired distance from the wall (meters)

    def scan_callback(self, msg):
        ranges = np.array(msg.ranges)

        # Clamp invalid values
        ranges = np.clip(ranges, msg.range_min, msg.range_max)

        self.right_distance = np.mean(ranges[250:290])  # right side (~270°)
        self.front_distance = np.mean(ranges[0:10].tolist() + ranges[-10:])  # front (~0°)

    def control_loop(self):
        msg = Twist()
        error = self.target_distance - self.right_distance

        # Basic wall following logic
        Kp = 1.0  # Proportional gain
        linear_speed = 0.15
        angular_speed = Kp * error

        # Avoid frontal collision
        if self.front_distance < 0.4:
            msg.linear.x = 0.0
            msg.angular.z = 0.5  # turn left
        else:
            msg.linear.x = linear_speed
            msg.angular.z = angular_speed

        self.cmd_pub.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = WallFollower()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

