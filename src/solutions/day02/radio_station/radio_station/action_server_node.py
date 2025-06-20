from rclpy.node import Node
from rclpy.action import ActionServer
from radio_station_interfaces.action import ChooseSong
import rclpy
import time

class ActionServerNode(Node):

    def __init__(self):
        super().__init__('action_server_node')
        self.get_logger().info("Action Server Node is live!")
        self._srv = ActionServer(self, ChooseSong, 'choose_song', self.execute_cb)
    
    async def execute_cb(self, goal_handle):
        song = goal_handle.request.song_name
    
        for pct in range(0, 101, 10):
            feedback = ChooseSong.Feedback()
            feedback.progress_pct = float(pct)
            feedback.status_line = f"Playing {song} - {pct}%"
            goal_handle.publish_feedback(feedback)
            time.sleep(1)
        
        goal_handle.succeed()
        res = ChooseSong.Result(success=True, final_message=f"Finished {song}")
        
        return res


def main(args=None):
    rclpy.init(args=args)
    node = ActionServerNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
