import rclpy
from rclpy.node import Node
from radio_station_interfaces.srv import GetNowPlaying

class NowPlayingClient(Node):
    def __init__(self):
        super().__init__('now_playing_client')
        self.client = self.create_client(GetNowPlaying, 'get_now_playing')

        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Waiting for now playing service...')

        self.request = GetNowPlaying.Request()
        self.send_request()

    def send_request(self):
        future = self.client.call_async(self.request)
        future.add_done_callback(self.handle_response)

    def handle_response(self, future):
        try:
            response = future.result()
            self.get_logger().info(
                f"Now Playing:\n"
                f"Station: {response.station_name}\n"
                f"Song: {response.song_title}\n"
                f"Artist: {response.artist_name}\n"
            )
        except Exception as e:
            self.get_logger().error(f'Service call failed: {e}')
        finally:
            self.get_logger().info("Shutting down client node.")
            rclpy.shutdown()


def main(args=None):
    rclpy.init(args=args)
    node = NowPlayingClient()
    rclpy.spin(node)

if __name__ == '__main__':
    main()
