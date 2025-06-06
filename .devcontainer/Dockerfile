# ─────────────────────────────────────────────────────────────
# Base: Official ROS 2 Humble image
# ─────────────────────────────────────────────────────────────
FROM ros:humble

# ─────────────────────────────────────────────────────────────
# 1 Remove EVERY ROS source shipped in the base image
#   (there are two: ros2.list and ros2-latest.list)
#   → apt will not contact the broken mirror in the next step.
# ─────────────────────────────────────────────────────────────
RUN find /etc/apt/sources.list.d -type f -name '*ros*' -delete

# ─────────────────────────────────────────────────────────────
# 2 Install curl & gnupg from Ubuntu repos (these still work)
# ─────────────────────────────────────────────────────────────
RUN apt-get update && \
    apt-get install -y --no-install-recommends curl gnupg lsb-release

# ─────────────────────────────────────────────────────────────
# 3 Fetch the refreshed Open Robotics key
#   and recreate a single clean ROS source that uses it
# ─────────────────────────────────────────────────────────────
RUN curl -fsSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key \
    | gpg --dearmor -o /usr/share/keyrings/ros-archive-keyring.gpg && \
    echo "deb [signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] \
         http://packages.ros.org/ros2/ubuntu $(lsb_release -cs) main" \
    > /etc/apt/sources.list.d/ros2.list

# ─────────────────────────────────────────────────────────────
# 4 Now the key is valid → refresh metadata & install packages
# ─────────────────────────────────────────────────────────────
RUN apt-get update && \
    apt-get install -y ros-humble-kobuki-ros-interfaces


# ─────────────────────────────────────────────────────────────
# Install useful packages and ROS tools
# ─────────────────────────────────────────────────────────────
RUN apt update && apt install -y \
    python3-pip \
    python3-colcon-common-extensions \
    python3-vcstool \
    git \
    curl \
    nano \
    lsb-release \
    ros-humble-rqt* \
    ros-humble-turtlesim \
    ros-humble-demo-nodes-py \
    bash-completion \
    && rm -rf /var/lib/apt/lists/*


# ─────────────────────────────────────────────────────────────
# Set up a non-root user for development
# ─────────────────────────────────────────────────────────────
RUN useradd -m dev && echo "dev ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

USER dev
WORKDIR /home/dev

# ─────────────────────────────────────────────────────────────
# Environment Variables
# ─────────────────────────────────────────────────────────────
ENV ROS_VERSION=2
ENV ROS_DISTRO=humble
ENV ROS_DOMAIN_ID=0
ENV DEBIAN_FRONTEND=noninteractive

# Source ROS 2 setup script by default
SHELL ["/bin/bash", "-c"]
RUN echo "source /opt/ros/humble/setup.bash" >> /home/dev/.bashrc && \
    echo "source /etc/bash_completion" >> /home/dev/.bashrc && \
    chown dev:dev /home/dev/.bashrc
