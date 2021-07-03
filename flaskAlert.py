import telegram
import logging

from flask import Flask
from flask import request
from datetime import datetime

logger = logging.getLogger(__name__)

app = Flask(__name__)
app.secret_key = "aYT>.L$kk2h>!"

CHAT_ID = "chatID"
TOKEN = "botToken"

bot = telegram.Bot(token=TOKEN)


@app.route("/alert", methods=["POST"])
def postAlertmanager():

    content = request.get_json()

    if not content:
        abort(400)

    alert = content["alerts"][0]
    alert_name = alert["labels"]["alertname"]
    # just strip microseconds part
    d = alert["startsAt"].split(".")[0]
    alert_time = str(datetime.strptime(d, "%Y-%m-%dT%H:%M:%S"))
    alert_high = alert["labels"]["severity"].upper()
    alert_inst = alert["labels"].get("instance")
    # assume desciption may be empty

    message = "[{}] {} at {}\non {}\n".format(
        alert_high, alert_name, alert_time, alert_inst
    )

    for annotation in alert["annotations"]:
        message += "{}: {}\n".format(
            annotation, alert["annotations"][annotation]
        )
    bot.sendMessage(chat_id=CHAT_ID, text=message)

    return ""


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9119)
