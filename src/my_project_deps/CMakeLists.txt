cmake_minimum_required(VERSION 3.5)
project(turtlebot3_project)

# Find required packages
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(xacro REQUIRED)
find_package(gazebo_ros_pkgs REQUIRED)
find_package(gazebo_ros2_control REQUIRED)
find_package(turtlebot3_gazebo REQUIRED)
find_package(turtlebot3_teleop REQUIRED)
find_package(turtlebot3_simulator REQUIRED)
find_package(rviz2 REQUIRED)
find_package(navigation2 REQUIRED)
find_package(slam_toolbox REQUIRED)
find_package(robot_state_publisher REQUIRED)
find_package(tf2_tools REQUIRED)

# Add your custom executable or libraries here
# add_executable(my_node src/my_node.cpp)

# Install the launch files, URDF, and other resources
install(DIRECTORY urdf/
  DESTINATION share/${PROJECT_NAME}/urdf
)

install(DIRECTORY launch/
  DESTINATION share/${PROJECT_NAME}/launch
)

ament_package()
