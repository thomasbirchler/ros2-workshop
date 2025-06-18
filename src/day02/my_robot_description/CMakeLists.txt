cmake_minimum_required(VERSION 3.5)
project(my_robot_description)

find_package(ament_cmake REQUIRED)

# Install the URDF/Xacro files
install(DIRECTORY urdf/
  DESTINATION share/${PROJECT_NAME}/urdf
)

# Install the launch files
install(DIRECTORY launch/
  DESTINATION share/${PROJECT_NAME}/launch
)

ament_package()
