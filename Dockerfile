FROM python:3.9-alpine

EXPOSE 9119

CMD ["./run.sh"]

WORKDIR /alertmanager-webhook-telegram

COPY requirements.txt /alertmanager-webhook-telegram/

RUN set -xe ;\
    apk update ;\
    apk add bash ;\
    pip install -r requirements.txt

COPY docker/run.sh *.py /alertmanager-webhook-telegram/

RUN chmod +x run.sh
