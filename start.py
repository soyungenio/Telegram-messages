# -*- coding: utf-8 -*- 
from pytg.utils import coroutine

from pytg.sender import Sender
from pytg.receiver import Receiver
receiver = Receiver(host="127.0.0.1", port=5698)
sender = Sender(host="127.0.0.1", port=5698)

#sender.send_msg("Дима1", "Hello World!")

@coroutine 
def main_loop():
    try:
        while True: # loop for a session.
            msg = (yield) # it waits until it got a message, stored now in msg.
            print("Message: ", msg)
            if "text" in msg:
                if msg["own"] is False and msg["own"] is 'message':
                    sender.send_msg("Дима1", "Hello World!")
            else if msg["type"]["photo"]:
                res = receiver.load_photo(msg[id])
                print(res)
            
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