import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class Publisher_Node(Node):
    def __init__(self):
        super().__init__('publisher_node')
        self.get_logger().info("Node started!")
        # Fill in the missing msg type, topic name, and queue size
        self.publisher_ = self.create_publisher(msg_type=, topic= , queue_size=)
        self.timer = self.create_timer(1.0, self.timer_callback)
        # We will use this variable to count the number of messages sent
        self.i = 0

    def timer_callback(self):
        msg = String()
        # Add a string to the msg.data field
        msg.data = 
        # Fill out the missing code to publish the message
        self.publisher_.publish()

        self.i += 1
        self.get_logger().info(f'Publishing: "{msg.data}", since {self.i} seconds.')

def main():
    rclpy.init()
    # Create an instance of the Publisher_Node class
    node = 
    rclpy.spin(node)
    rclpy.shutdown()
