# -*- coding: utf-8 -*-
from pytg.utils import coroutine

from pytg.sender import Sender
from pytg.receiver import Receiver
receiver = Receiver(host="127.0.0.1", port=5698)
sender = Sender(host="127.0.0.1", port=5698)

#sender.send_msg("▒^▒има1", "Hello World!")

@coroutine
def main_loop():
    try:
        while True: # loop for a session.
            msg = (yield) # it waits until it got a message, stored now in msg.
            print("Message: ", msg)
            if "text" in msg:
                if msg["own"] is False and  "message" in str(msg):
                    sender.send_msg("Marat_Gaptullin", msg.text, enable_preview=True)
            elif "photo" in str(msg):   
                if msg["own"] is False and  "message" in str(msg):
                    res = sender.load_photo(msg["id"])
                    sender.send_photo("Marat_Gaptullin", res)
            elif "video" in str(msg):
                if msg["own"] is False and  "message" in str(msg):
                    res = sender.load_video(msg["id"])
                    sender.send_video("Marat_Gaptullin", res)
            # do more stuff here!

    except GeneratorExit:
        # the generator (pytg) exited (got a KeyboardIterrupt).
        pass
    except KeyboardInterrupt:
        # we got a KeyboardIterrupt(Ctrl+C)
        pass
    else:
        # the loop exited without exception, becaues _quit was set True
        pass
#

# start the Receiver, so we can get messages!
receiver.start()

# let "main_loop" get new message events.
# You can supply arguments here, like main_loop(foo, bar).
receiver.message(main_loop())
# now it will call the main_loop function and yield the new messages.