import rclpy
from rclpy.node import Node
from radio_communication_solutions_interfaces.srv import GetNowPlaying
from datetime import datetime

class NowPlayingService(Node):
    def __init__(self):
        super().__init__('now_playing_service')
        self.srv = self.create_service(GetNowPlaying, 'get_now_playing', self.handle_now_playing)
        self.get_logger().info("Now Playing Service is live!")

    def handle_now_playing(self, request, response):
        response.station_name = "102 FM"
        response.song_title = "Bohemian Rhapsody"
        response.artist_name = "Queen"
        response.time_played = datetime.now().strftime("%H:%M:%S")
        self.get_logger().info("Returned current track info.")
        return response

def main(args=None):
    rclpy.init(args=args)
    rclpy.spin(NowPlayingService())
    rclpy.shutdown()

if __name__ == '__main__':
    main()
