FROM ubuntu:latest

# Set non-interactive frontend
ENV DEBIAN_FRONTEND=noninteractive

# Update and upgrade packages
RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y nano iputils-ping git python3 wget libpcap-dev openssh-server openssh-client net-tools

# Create symbolic link to set python3 as python
RUN ln -s /usr/bin/python3 /usr/bin/python

# Allow ssh connections 
EXPOSE 22

# Download get-pip.py and install pip for python
RUN wget -O - https://bootstrap.pypa.io/get-pip.py | python

# Clone the repository from GitHub
RUN git clone https://github.com/BenIlies/NoPASARAN.git

# Set working directory to NoPASARAN
WORKDIR /NoPASARAN

# Install Python dependencies
RUN python -m pip install -r requirements.txt