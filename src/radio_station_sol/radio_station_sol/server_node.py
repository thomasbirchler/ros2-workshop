import rclpy, time
from rclpy.action import ActionServer
from rclpy.node   import Node
from radio_station_interfaces_sol.action import ChooseSong

class RadioDJ(Node):
    def __init__(self):
        super().__init__('radio_dj')
        self._srv = ActionServer(
            self,
            ChooseSong,
            'choose_song',
            self.execute_callback)

    async def execute_callback(self, goal_handle):
        song = goal_handle.request.song_name
        self.get_logger().info(f"Got a request for: {song}")

        feedback = ChooseSong.Feedback()
        for pct in range(0, 101, 20):
            feedback.progress_pct = float(pct)
            feedback.status_line  = f"Playing {song} – {pct}%"
            goal_handle.publish_feedback(feedback)
            time.sleep(1.0)

        result = ChooseSong.Result()
        result.success = True
        result.final_message = f"Finished playing {song}!"
        self.get_logger().info(result.final_message)
        return result

def main():
    rclpy.init()
    node = RadioDJ()
    rclpy.spin(node)

if __name__ == '__main__':
    main()
