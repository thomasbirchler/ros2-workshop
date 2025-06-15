cmake_minimum_required(VERSION 3.5)
project(radio_station_interfaces_sol)

find_package(ament_cmake REQUIRED)
find_package(rosidl_default_generators REQUIRED)

rosidl_generate_interfaces(${PROJECT_NAME}
  "action/ChooseSong.action"
)

ament_package()
