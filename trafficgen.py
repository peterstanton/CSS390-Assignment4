import sys
import time
from time import sleep
import subprocess
import random

url = sys.argv[1]
rps = int(sys.argv[2])
jitter = float(sys.argv[3])

if jitter < 0:
    jitter = 0.1
elif jitter > 1:
    jitter = 1.0

lower = int(rps * (1.0 - jitter))
upper = int(rps * (1.0 + jitter))
print lower
print upper

invoke = "curl -G " + url

invoke = invoke.split(" ")

permGood = invoke[2]

while True:
    actual = random.randint(lower, upper)
    start = time.time()
    interval = 1
    for i in range(actual):
	print str(i)
        invoke[2] = permGood
        chance = random.randint(0, 100)
        if chance in range(0, 5):
            invoke[2] = invoke[2] + '/arglebargle'
            process = subprocess.call(invoke)
        elif chance in range(6, 10):
            invoke[2] += "/fail"
            process = subprocess.call(invoke)
        else:
            process = subprocess.call(invoke)
    end = time.time()
    if(1-(start-end)) > 0:
    	sleep(1-(start-end))
    else:
	continue
