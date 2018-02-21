# -*- coding: utf-8 -*- 
from pytg import Telegram
from pytg.utils import coroutine

tg = Telegram(
	telegram="/root/tg/bin/telegram-cli",
	pubkey_file="/root/tg/tg-server.pub")
receiver = tg.receiver
sender = tg.sender

#sender.send_msg("Дима1", "Hello World!")

@coroutine 
def main_loop():
	while not QUIT:
		msg = (yield) # it waits until it got a message, stored now in msg.
		print("Message: ", msg.text)
		# do more stuff here!
	#
#

# start the Receiver, so we can get messages!
receiver.start()

# let "main_loop" get new message events.
# You can supply arguments here, like main_loop(foo, bar).
receiver.message(main_loop())
# now it will call the main_loop function and yield the new messages.