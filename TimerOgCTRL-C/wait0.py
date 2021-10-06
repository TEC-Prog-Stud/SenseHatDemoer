
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
    print(f"@ {datetime.datetime.now()}, afslutter med signum={signum} efter {count} omgange")
    sys.exit(0)

def gentagelse():
    global count
    count += 1
    print(f"@ {datetime.datetime.now()}, fortsætter efter {count} omgange")
    

while True:
    gentagelse()
    time.sleep(0.3)

afslutning(None, None)