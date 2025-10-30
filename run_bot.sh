#!/bin/bash
python oneshot.py -m 'Bot Started'
python en_bot.py
python oneshot.py -m 'Bot Crashed or was turned off'