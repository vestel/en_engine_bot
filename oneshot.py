import requests  # pip install pyTelegramBotAPI
import configparser
import argparse

from datetime import datetime

# Читаем конфиг
config = configparser.ConfigParser()
config.read('settings.ini')
TOKEN = config['Settings']['Token']
REPORT_TO = config['Settings']['ReportTo']


parser = argparse.ArgumentParser(
                    prog='OneShot Telegram Notifier',
                    description='What the program does',
                    epilog='Text at the bottom of help')
parser.add_argument('-m', '--message', type=str, required=True)
parser.add_argument('-c', '--chat', type=str, required=False, default=REPORT_TO)

args = parser.parse_args()
chat_id = int(args.chat)
message = args.message

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
payload = {"chat_id": chat_id, "text": message}
response = requests.post(url, data=payload)

if response.status_code != 200:
    raise Exception(f"Error {response.status_code}: {response.text}")
else:
    print(f"Message sent to {chat_id}: {message}")

