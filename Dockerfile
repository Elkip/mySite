FROM python:3.8

WORKDIR /app
ADD . /app

ARG APP_USER=uwsgi
RUN groupadd -r ${APP_USER} && useradd --no-log-init -r -g ${APP_USER} ${APP_USER}

RUN apt-get -y update \
    && pip install --upgrade pip  \
    && apt-get -y install build-essential net-tools \
    && pip install -r requirements.txt \
    && rm -rf /var/cache/apk/*

# Expose 8081 for the uwsgi development stats page
# EXPOSE 8081

# Change to a non-root user
USER ${APP_USER}:${APP_USER}

CMD [ "uwsgi", "--ini", "/app/uwsgi.ini" ]
