FROM ubuntu:16.04

WORKDIR /home

RUN apt-get update
RUN apt-get install python3 python3-tk python3-pip -y

RUN apt-get install git -y

RUN git clone https://github.com/noeul1114/streami.git

WORKDIR /home/streami
RUN git fetch --all && git reset --hard && git pull


RUN pip3 install -r requirements.txt

CMD bash -c "python3 main.py"
