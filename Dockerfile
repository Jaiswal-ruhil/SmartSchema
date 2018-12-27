FROM ubuntu
RUN apt update
RUN apt install python3 python3-pip -y
RUN pip3 install python3-SmartSchema --user