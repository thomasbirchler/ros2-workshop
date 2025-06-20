from rclpy.node import Node
from std_msgs.msg import String
import rclpy

class Listener(Node):
    def __init__(self):
        super().__init__('listener_sol')
        self.subscription = self.create_subscription(String, 'radio/frequency_100_3', self.listener_callback, 10)
    
    def listener_callback(self, msg):
        self.get_logger().info(f'I heard: "{msg.data}"')


def main():
    rclpy.init()
    node = Listener()
    rclpy.spin(node)
    rclpy.shutdown()
