import sys
import time
from time import sleep
import subprocess
import random

url = sys.argv[1]
rps = int(sys.argv[2])
jitter = float(sys.argv[3])

lower = rps * (1.0 - jitter)
upper = rps * (1.0 + jitter)

invoke = "curl -G " + url

invoke = invoke.split(" ")

permGood = invoke[2]

while True:
    actual = random.randint(lower, upper)
    start = time.time()
    interval = 1
    for i in range(actual):
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
    sleep(1-(start-end))
