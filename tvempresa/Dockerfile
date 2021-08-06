FROM python:3.6-alpine

ENV PYTHONUNBUFFERED 1

RUN apk --update add \
    build-base \
    postgresql \
    postgresql-dev \
    libpq \
    # pillow dependencies
    jpeg-dev \
    zlib-dev \
    # pycurl dependencies
    curl-dev



RUN mkdir /www
WORKDIR /www
RUN mkdir /requirements
COPY ./requirements/ ./requirements
RUN pip install -r ./requirements/dev.txt



COPY . /www/
