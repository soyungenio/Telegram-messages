# -*- coding: utf-8 -*- 
from pytg import Telegram
tg = Telegram(
	telegram="/root/tg/bin/telegram-cli",
	pubkey_file="/root/tg/tg-server.pub")
receiver = tg.receiver
sender = tg.sender

sender.send_msg("Дима1", "Hello World!")