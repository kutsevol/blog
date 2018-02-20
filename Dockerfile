FROM python:latest
# New style declare MAINTAINER
LABEL maintainer="arthur.kutsevol@gmail.com"

RUN mkdir /app
WORKDIR /app

# For speed up build by using caches effectively (best practices)
ADD requirements.txt Makefile /app/
RUN make pip-install

ADD . .

RUN mv my_site/settings/secret_settings.py.sample my_site/settings/secret_settings.py

# So as not to create additional layers to reduce the size of the image
RUN make migrate && make static

EXPOSE 8000
CMD make run
