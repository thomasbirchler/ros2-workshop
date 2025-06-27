from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
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
            arguments=['-d', 'rviz/tf_view.rviz'],
            output='screen'
        )
    ])
