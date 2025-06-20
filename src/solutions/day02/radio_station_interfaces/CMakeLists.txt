cmake_minimum_required(VERSION 3.5)
project(radio_station_interfaces)

find_package(ament_cmake REQUIRED)
find_package(rosidl_default_generators REQUIRED)

rosidl_generate_interfaces(${PROJECT_NAME}
"srv/GetNowPlaying.srv"
"action/ChooseSong.action"
)

ament_export_dependencies(rosidl_default_runtime)
ament_package()