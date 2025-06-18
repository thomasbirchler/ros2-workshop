import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class Broadcaster(Node):
    def __init__(self):
        super().__init__('broadcaster_sol')
        self.get_logger().info("Node started!")
        self.publisher_ = self.create_publisher(String, '/radio/frequency_102', 10)
        self.timer = self.create_timer(1.0, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = String()
        msg.data = f'We are broadcasting on frequency 102 FM since {self.i} seconds.'
        self.i += 1
        self.publisher_.publish(msg)

def main():
    rclpy.init()
    node = Broadcaster()
    rclpy.spin(node)
    rclpy.shutdown()
