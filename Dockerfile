FROM ubuntu:bionic
RUN apt-get -y update
RUN apt-get -y install apt-utils
RUN apt-get -y install python3.8
RUN apt-get -y install python-yara
CMD ["bash"]
