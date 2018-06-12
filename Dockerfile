FROM alpine:3.7

COPY docker/run.sh *.py requirements.txt /alertmanager-webhook-telegram/

WORKDIR /alertmanager-webhook-telegram

RUN set -xe ;\
    apk update ;\
    apk add git py-pip bash ;\
    pip install -r requirements.txt ;\
    chmod +x run.sh

EXPOSE 9119

ENTRYPOINT ["./run.sh"]
