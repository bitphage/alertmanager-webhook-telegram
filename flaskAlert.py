import telegram
import logging

from flask import Flask
from flask import request
from datetime import datetime

logger = logging.getLogger(__name__)

app = Flask(__name__)
app.secret_key = 'aYT>.L$kk2h>!'

CHAT_ID = 'chatID'
TOKEN = 'botToken'

bot = telegram.Bot(token=TOKEN)

@app.route('/alert', methods = ['POST'])
def postAlertmanager():

    content = request.get_json()

    if not content:
        abort(400)

    alert_name = content['alerts'][0]['labels']['alertname']
    # just strip microseconds part
    d = content['alerts'][0]['startsAt'].split('.')[0]
    alert_time = str(datetime.strptime(d, '%Y-%m-%dT%H:%M:%S'))
    alert_high = content['alerts'][0]['labels']['severity'].upper()
    alert_inst = content['alerts'][0]['labels']['instance']
    # assume desciption may be empty
    alert_desc = content['alerts'][0]['annotations'].get('description', None)

    message = '[{}] {} at {}\non {} \n{}'.format(
            alert_high, alert_name, alert_time, alert_inst, alert_desc)
    bot.sendMessage(chat_id=CHAT_ID, text=message)

    return ''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9119)
