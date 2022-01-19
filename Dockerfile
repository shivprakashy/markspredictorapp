FROM alpine:latest

RUN apk add --no-cache --update python3 py3-pip bash
ADD ./requirements.txt /tmp/requirements.txt

RUN pip3 install --no-cache-dir -q -r /tmp/requirements.txt

ADD ./ /opt/

WORKDIR /opt/

RUN adduser -D myuser
USER myuser

CMD gunicorn --bind 0.0.0.0:$PORT wsgi
