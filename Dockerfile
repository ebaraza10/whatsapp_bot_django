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
RUN apk add busybox-extras
RUN apk add --no-cache jpeg-dev zlib-dev

RUN apk add gcc musl-dev python3-dev libffi-dev openssl-dev cargo
# install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN mkdir -p static
RUN mkdir -p staticfiles

RUN echo yes | python3 manage.py collectstatic
RUN python3 manage.py makemigrations
RUN python3 manage.py migrate
RUN mkdir -p bot/migrations
RUN touch bot/migrations/__init__.py || exit