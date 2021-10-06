
"""
Se: 
https://docs.python.org/3/library/signal.html#signal.signal
https://docs.python.org/3/library/signal.html#signal.setitimer

og nogen eksempler...
https://python.hotexamples.com/examples/signal/-/setitimer/python-setitimer-function-examples.html

"""

import signal
import datetime
import time
import sys

count = 0

def afslutning(signum, frame):
    global count
    signal.setitimer(signal.ITIMER_REAL, 0) # Disable the alarm
    print(f"@ {datetime.datetime.now()}, afslutter med signum={signum} efter {count} omgange")
    time.sleep(2)
    sys.exit(0)

signal.signal(signal.SIGTERM, afslutning)
signal.signal(signal.SIGINT, afslutning)

def gentagelse(signum, frame):
    global count
    count += 1
    #print(f"@ {datetime.datetime.now()}, fortsætter efter {count} omgange")

# while True:
#     gentagelse()
#     time.sleep(0.5)

signal.signal(signal.SIGALRM, gentagelse)
signal.setitimer(signal.ITIMER_REAL, 2, 0.01)

while True:
    signal.pause()

signal.setitimer(signal.ITIMER_REAL, 0) # Disable the alarm



