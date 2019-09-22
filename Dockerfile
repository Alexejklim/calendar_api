FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY req.txt /code/
RUN pip install -r req.txt
COPY . /code/
RUN apt-get update
RUN apt-get -y install redis-server
EXPOSE 8000
