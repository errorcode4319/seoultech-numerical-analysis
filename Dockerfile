FROM ubuntu:22.04

RUN apt update && apt -y install python3 python3-pip

RUN pip3 install jupyter 

# Numerical Analysis Libraries
RUN pip3 install numpy matplotlib scipy