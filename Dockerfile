FROM ubuntu:14.04
RUN apt-get update -y
RUN apt-get install -y apt-transport-https
RUN apt-get install -y python3.5 python3-pip
COPY requirements.txt /
RUN pip3 install -r /requirements.txt
COPY . /app
WORKDIR /app
CMD ["python3", "./app.py"]