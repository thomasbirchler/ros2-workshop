from rclpy.node import Node
from rclpy import init, spin
from radio_communication_solutions_interfaces.srv import AddTwoInts

class MinimalService(Node):
    def __init__(self):
        super().__init__('minimal_service')
        self.srv = self.create_service(AddTwoInts, 'add_two_ints', self.add_callback)

    def add_callback(self, request, response):
        response.sum = request.a + request.b
        self.get_logger().info(f"Received request: {request.a} + {request.b}")
        return response

def main(args=None):
    init(args=args)
    node = MinimalService()
    try:
        spin(node)
    except KeyboardInterrupt:
        pass
