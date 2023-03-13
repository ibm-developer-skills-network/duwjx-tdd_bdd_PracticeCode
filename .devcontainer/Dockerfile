# Image to simulate Skills Network cloud environment
FROM ubuntu:18.04

ENV DEBIAN_FRONTEND=noninteractive

# Add repository for Python 3.8
RUN apt-get update && \
    apt-get install -y software-properties-common dirmngr apt-transport-https lsb-release ca-certificates && \
    add-apt-repository -y ppa:deadsnakes/ppa

# Add tools and Python 3.8
RUN apt-get update && \
    apt-get install -y sudo vim git zip tree curl wget python3.8-dev python3-pip && \
    update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.8 1 && \
    apt-get autoremove -y && \
    apt-get clean -y

# Create a user for development
ARG USERNAME=theia
ARG USER_UID=1000
ARG USER_GID=$USER_UID

# Create the user with passwordless sudo privileges
RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME -s /bin/bash \
    && usermod -aG sudo $USERNAME \
    && echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
    && chmod 0440 /etc/sudoers.d/$USERNAME

# Set up the Python development environment
WORKDIR /project
RUN python3 -m pip install --upgrade pip && \
    pip3 install --upgrade wheel

# Enable color terminal for docker exec bash
ENV TERM=xterm-256color

EXPOSE 8000

# Become a regular user for development
USER $USERNAME
