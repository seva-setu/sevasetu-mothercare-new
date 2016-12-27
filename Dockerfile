FROM python:2.7-alpine

ADD . /application

RUN pip install -r /application/requirements.txt

EXPOSE 80

WORKDIR /application

CMD python server.py
