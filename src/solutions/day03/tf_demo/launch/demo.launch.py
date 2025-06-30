from launch import LaunchDescription
from launch_ros.actions import Node
import os
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():
    rviz_config_path = os.path.join(
        get_package_share_directory('tf_demo'),
        'rviz',
        'tf_view.rviz'
    )
    
    return LaunchDescription([
        Node(
            package='tf_demo',
            executable='static_tf_pub',
            name='static_tf_pub'
        ),
        Node(
            package='tf_demo',
            executable='dynamic_tf_pub',
            name='dynamic_tf_pub'
        ),
        Node(
            package='rviz2',
            executable='rviz2',
            arguments=['-d', rviz_config_path],
            output='screen'
        )
    ])
