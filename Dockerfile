FROM ubuntu:bionic
RUN apt-get -y update
RUN apt-get -y install apt-utils
RUN apt-get -y install openssh-client
RUN apt-get -y install python3.8
RUN apt-get -y install python-yara
RUN apt-get -y install python3-pip
RUN pip3 install --upgrade pip
RUN pip3 install setuptools-rust
RUN pip3 install fabric
RUN pip3 install requests
CMD ["bash"]
