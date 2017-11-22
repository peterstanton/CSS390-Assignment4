import sys
import time
import subprocess
import random

url = sys.argv[1]
rps = int(sys.argv[2])
jitter = float(sys.argv[3])

lower = rps * (1.0 - jitter)
upper = rps * (1.0 + jitter)

actual = random.randint(lower, upper)

invoke = "curl -G " + url

invoke = invoke.split(" ")

while True:
    start = time.time()
    interval = 1
    for i in range(actual):
        chance = random.randint(0, 100)
        if chance in range(0, 5):
            invoke += 'arglebargle'
            process = subprocess.call(invoke)
        elif chance in range(6, 10):
            invoke += '/fail'
            process = subprocess.call(invoke)
        else:
            process = subprocess.call(invoke)

