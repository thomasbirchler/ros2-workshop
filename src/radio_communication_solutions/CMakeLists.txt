cmake_minimum_required(VERSION 3.5)
project(radio_communication_solutions)

find_package(ament_cmake REQUIRED)
find_package(ament_cmake_python REQUIRED)
find_package(rosidl_default_generators REQUIRED)

rosidl_generate_interfaces(${PROJECT_NAME}
  "srv/GetNowPlaying.srv"
  "srv/AddTwoInts.srv"
)

ament_package()
