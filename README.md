# Alertmanager webhook for Telegram using Flask 

Bot is intended to send alertmanager notifications to a specified `chatID`.

## INSTALL

* pip install -r requirements.txt

Change on flaskAlert.py
=======================
* botToken
* chatID
  
Alertmanager configuration example
==================================

```yaml
receivers:
  - name: 'telegram-webhook'
    webhook_configs:
    - url: http://ipFlaskAlert:9119/alert
      send_resolved: true

```

One way to get the chat ID
==========================
1) Add bot on channel
2) Send message on this channel with @botname
3) Access access the link https://api.telegram.org/botXXX:YYYY/getUpdates (xxx:yyyy botID)

Running
=======
* python flaskAlert.py

Running on docker
=================

```
docker run -d -e bottoken="telegramBotToken" -e chatid="telegramChatID" -p 9119:9119 vvk123/alertmanager-webhook-telegram:latest
```
