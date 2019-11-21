# pull official base image
FROM alpine:latest

# set work directory
ENV APP_HOME=/usr/src/app
WORKDIR ${APP_HOME}
ADD . ${APP_HOME}

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1



RUN apk add --no-cache jpeg-dev zlib-dev
RUN apk add --update py3-pip

# install dependencies
RUN pip install -r requirements.txt
