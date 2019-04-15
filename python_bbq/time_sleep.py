from datetime import datetime
from time import sleep
from random import randint

for i in range(3):
    odds = [i for i in range(1, 60, 2)]

    right_this_minute = datetime.today().minute

    if right_this_minute in odds:
        print("this minute seems a little odd!!")
    else:
        print("not an odd minute")
    wait = randint(1, 30)
    sleep(wait)
