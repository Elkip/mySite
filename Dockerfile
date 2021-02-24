FROM python:3.8

WORKDIR /app
ADD . /app

RUN apt-get -y update \
    && pip install --upgrade pip  \
    && apt-get -y install build-essential net-tools \
    && pip install -r requirements.txt \
    && rm -rf /var/cache/apk/*

EXPOSE 80
EXPOSE 8080

CMD [ "uwsgi", "--ini", "/app/uwsgi.ini" ]
