import rclpy
from rclpy.action   import ActionClient
from rclpy.node     import Node
from radio_station_interfaces_sol.action import ChooseSong

class SongRequester(Node):
    def __init__(self, song):
        super().__init__('song_requester')
        self._action_client = ActionClient(self, ChooseSong, 'choose_song')
        self._song = song
        self._action_client.wait_for_server()
        self.send_request() 

    def send_request(self):
        goal = ChooseSong.Goal(song_name=self._song)
        self._send_future = self._action_client.send_goal_async(
            goal,
            feedback_callback=self.feedback_cb)
        self._send_future.add_done_callback(self.goal_response_cb)

    def feedback_cb(self, feedback_msg):
        fb = feedback_msg.feedback
        self.get_logger().info(f"DJ says: {fb.status_line}")

    def goal_response_cb(self, future):
        goal_handle = future.result()
        result_future = goal_handle.get_result_async()
        result_future.add_done_callback(self.result_cb)

    def result_cb(self, future):
        result = future.result().result
        self.get_logger().info(f"DJ final: {result.final_message}")
        rclpy.shutdown()

def main():
    rclpy.init()
    requester = SongRequester("Bohemian Rhapsody")
    rclpy.spin(requester)

if __name__ == '__main__':
    main()
