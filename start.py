# -*- coding: utf-8 -*- 
from pytg.utils import coroutine

from pytg.sender import Sender
from pytg.receiver import Receiver
receiver = Receiver(host="localhost", port=4458)
sender = Sender(host="localhost", port=4458)

#sender.send_msg("Дима1", "Hello World!")

@coroutine 
def main_loop():
    msg = (yield) # it waits until it got a message, stored now in msg.
    print("Message: ", msg)
		# do more stuff here!
	#
#

# start the Receiver, so we can get messages!
receiver.start()

# let "main_loop" get new message events.
# You can supply arguments here, like main_loop(foo, bar).
receiver.message(main_loop())
# now it will call the main_loop function and yield the new messages.