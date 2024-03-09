FROM ubuntu:22.04

RUN apt update && apt -y install python3 python3-pip

RUN pip3 install jupyter 

EXPOSE 8888