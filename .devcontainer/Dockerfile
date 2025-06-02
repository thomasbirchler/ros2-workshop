# ─────────────────────────────────────────────────────────────
# Base: Official ROS 2 Humble image
# ─────────────────────────────────────────────────────────────
FROM ros:humble

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
