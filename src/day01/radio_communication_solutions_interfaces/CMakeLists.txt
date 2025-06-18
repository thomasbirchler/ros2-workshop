cmake_minimum_required(VERSION 3.5)
project(radio_communication_solutions_interfaces)

find_package(ament_cmake REQUIRED)
find_package(rosidl_default_generators REQUIRED)

rosidl_generate_interfaces(${PROJECT_NAME}
  "srv/AddTwoInts.srv"
  "srv/GetNowPlaying.srv"
)

ament_export_dependencies(rosidl_default_runtime)
ament_package()
