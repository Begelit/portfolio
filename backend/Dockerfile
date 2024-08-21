FROM ubuntu:22.04

RUN apt-get update && apt-get install -y python3 python3-pip

RUN pip install Django
RUN pip install -U channels[daphne]

WORKDIR /backend
COPY . /backend

EXPOSE 8000

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]

# docker build -t backendportfolio:latest .
# sudo docker run -p 127.0.0.1:8001:8000 backendportfolio:latest