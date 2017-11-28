import sys
import time
from time import sleep
import subprocess
import random
import urllib2

url = sys.argv[1]
rps = int(sys.argv[2])
jitter = float(sys.argv[3])

if jitter < 0:
    jitter = 0.1
elif jitter > 1:
    jitter = 1.0

lower = int(rps * (1.0 - jitter))
upper = int(rps * (1.0 + jitter))
while True:
    actual = random.randint(lower, upper)
    start = time.time()
    interval = 1
    for i in range(actual):
        chance = random.randint(0, 100)
        try:
            if chance in range(0, 5):
                urllib2.urlopen(url + '/arglebargle')
            elif chance in range(6, 10):
                urllib2.urlopen(url + '/fail')
            else:
                urllib2.urlopen(url)
        except urllib2.HTTPError:
            continue
    end = time.time()
    if(1-(end-start)) > 0:
        sleep(1-(end-start))
    else:
        continue
