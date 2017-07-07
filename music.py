#!/usr/bin/env python

import time, random, os, threading, psutil

CHARACTERS = ['A', 'B', 'C', 'D', 'E',]
ECHO_INTERVALS = ['0.8', '0.7', '700', '0.25', '700', '0.3',]

def play_this(interval):
    character = random.choice(CHARACTERS)
    echos = ' '.join(ECHO_INTERVALS[:6])
    os.system("""for p in '{}'; do ( play -n synth 3 pluck $p echos {} & ); done""".format(character + str(interval), echos))

def start():
    while True:
        x = psutil.cpu_percent()
        while int(x) == 0:
            x = psutil.cpu_percent()
        interval = (int(x) / 10) % 7
        play_this(interval)
        time.sleep(interval)

def trigger():
    threading.Thread(target=start).start()
    threading.Thread(target=start).start()
    threading.Thread(target=start).start()
    threading.Thread(target=start).start()
    threading.Thread(target=start).start()
    threading.Thread(target=start).start()

if __name__ == "__main__":
    trigger()
