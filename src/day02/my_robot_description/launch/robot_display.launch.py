import os
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, LogInfo
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import xacro

def generate_launch_description():
    # Get the URDF file from the package
    urdf_file = os.path.join(
        get_package_share_directory('my_robot_package'),
        'urdf',
        'my_robot.xacro'
    )

    # Convert the xacro to URDF
    doc = xacro.parse(open(urdf_file))
    urdf = xacro.process_doc(doc)

    # Write the URDF to a temporary file
    urdf_path = '/tmp/my_robot.urdf'
    with open(urdf_path, 'w') as f:
        f.write(urdf)

    return LaunchDescription([
        # Publish URDF to robot_description parameter
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            parameters=[{'robot_description': urdf_path}]
        ),
        # Launch RViz2 to visualize the robot
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            output='screen',
            arguments=['-d', os.path.join(
                get_package_share_directory('my_robot_package'),
                'rviz',
                'default.rviz'
            )]
        ),
    ])
