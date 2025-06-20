from rclpy.node import Node
import rclpy
from radio_station_interfaces.srv import GetNowPlaying

class GetNowPlayingServer(Node):
    def __init__(self):
        super().__init__('get_now_playing_server')
        self.srv = self.create_service(
            GetNowPlaying,
            'get_now_playing',
            self.handle_request
        )
        self.get_logger().info("Get Now Playing Service is live!")

    def handle_request(self, request, response):
        response.station_name = "Radio Educativa 100.3 FM"
        response.song_title = "Bohemian Rhapsody"
        response.artist_name = "Queen"
        self.get_logger().info("Returned current track info.")
        return response
    
def main(args=None):
    rclpy.init(args=args)
    server = GetNowPlayingServer()
    rclpy.spin(server)
    rclpy.shutdown()

if __name__ == '__main__':
    main()