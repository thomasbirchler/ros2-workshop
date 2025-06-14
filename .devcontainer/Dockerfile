###############################################################################
# Base image
###############################################################################
FROM ros:humble

###############################################################################
# 0. Silence tzdata prompts
###############################################################################
ENV DEBIAN_FRONTEND=noninteractive

###############################################################################
# 1. Remove the stale ROS apt entries shipped in the base image
###############################################################################
RUN find /etc/apt/sources.list.d -type f -name '*ros*' -delete

###############################################################################
# 2. Install curl / gnupg so we can refresh the key
###############################################################################
RUN apt-get update && apt-get install -y --no-install-recommends \
        curl \
        gnupg \
        lsb-release && \
    rm -rf /var/lib/apt/lists/*

###############################################################################
# 3. Add the *new* Open-Robotics GPG key and a clean repo entry
###############################################################################
RUN curl -fsSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key \
    | gpg --dearmor -o /usr/share/keyrings/ros-archive-keyring.gpg && \
    echo "deb [signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] \
         http://packages.ros.org/ros2/ubuntu $(lsb_release -cs) main" \
    | tee /etc/apt/sources.list.d/ros2.list

###############################################################################
# 4-A. Core ROS + simulation / GUI stack  (desktop ⊃ rviz + gazebo)
###############################################################################
RUN apt-get update && apt-get install -y --no-install-recommends \
        ros-humble-desktop \   
        ros-humble-kobuki-ros-interfaces \
    && rm -rf /var/lib/apt/lists/*

###############################################################################
# 4-B. Build & dev utilities
###############################################################################
RUN apt-get update && apt-get install -y --no-install-recommends \
        python3-pip \
        python3-colcon-common-extensions \
        python3-vcstool \
        build-essential \
        cmake \
        git \
        bash-completion \
    && rm -rf /var/lib/apt/lists/*

###############################################################################
# 4-C. Extra system libraries (Boost random used in boot-camp code)
###############################################################################
RUN apt-get update && apt-get install -y --no-install-recommends \
        libboost-random-dev \
    && rm -rf /var/lib/apt/lists/*

###############################################################################
# 5. Non-root development user
###############################################################################
RUN useradd -m dev && echo "dev ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers
USER dev
WORKDIR /home/dev
SHELL ["/bin/bash", "-c"]

# Source ROS on every shell start
RUN echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc
RUN echo "source /ros2_ws/install/setup.bash" >> /root/.bashrc
