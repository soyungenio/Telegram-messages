# -*- coding: utf-8 -*-
from pytg.utils import coroutine

from pytg.sender import Sender
from pytg.receiver import Receiver
receiver = Receiver(host="127.0.0.1", port=5698)
sender = Sender(host="127.0.0.1", port=5698)


tosend = ["TestPriem"]
frompriem = ["Группа мям", "Тест группа"]

@coroutine
def main_loop():
    try:
        while True: # loop for a session.
            msg = (yield) # it waits until it got a message, stored now in msg.
            print("Message: ", msg)
            if "message" in str(msg):
                for priem in frompriem:
                    if msg["receiver"]["name"] in priem:
                        if "text" in msg:
                            if msg["own"] is True:
                                for send in tosend:
                                    sender.send_msg(send, msg.text, enable_preview=True)
                        elif "photo" in str(msg):
                            if msg["own"] is True:
                                res = sender.load_photo(msg["id"])
                                for send in tosend:
                                    sender.send_photo(send, res)
                        elif "video" in str(msg):
                            if msg["own"] is True:
                                res = sender.load_video(msg["id"])
                                for send in tosend:
                                    sender.send_video(send, res)
                        elif "document" in str(msg):
                            if msg["own"] is True:
                                res = sender.load_document(msg["id"])
                                for send in tosend:
                                    sender.send_document(send, res)

    except GeneratorExit:
        # the generator (pytg) exited (got a KeyboardIterrupt).
        pass
    except KeyboardInterrupt:
        # we got a KeyboardIterrupt(Ctrl+C)
        pass
    else:
        # the loop exited without exception, becaues _quit was set True
        pass

# start the Receiver, so we can get messages!
receiver.start()

# let "main_loop" get new message events.
# You can supply arguments here, like main_loop(foo, bar).
receiver.message(main_loop())
# now it will call the main_loop function and yield the new messages.