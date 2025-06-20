from rclpy.node import Node
from std_msgs.msg import String
import rclpy

class Subscriber_Node(Node):
    def __init__(self):
        super().__init__('subscriber_node')
        # Create a subscription with the correct message type, topic name, callback function and queue size
        self.subscription = self.create_subscription()

    def listener_callback(self, msg):
        self.get_logger().info(f'I heard: "{msg.data}"')


def main():
    rclpy.init()
    # Create an instance of the Listener class
    node = 
    rclpy.spin(node)
    rclpy.shutdown()
