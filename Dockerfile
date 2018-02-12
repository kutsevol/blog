FROM python:latest
LABEL maintainer="arthur.kutsevol@gmail.com"

RUN mkdir /app
WORKDIR /app

ADD requirements.txt /app
RUN make install-requirements

ADD . /app
CMD make run
