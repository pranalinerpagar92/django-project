FROM python:3

ENV PYTHONUNBUFFERED 1
#RUN mkdir /my_api
WORKDIR /my_api
ADD . /my_api
COPY . /my_api/
RUN pip install -r requirements.txt


