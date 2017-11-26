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

actual = random.randint(lower, upper)

invoke = "curl -G " + url

invoke = invoke.split(" ")

permGood = invoke[2]

while True:
    start = time.time()
    interval = 1
    for i in range(actual):
	invoke[2] = permGood
        chance = random.randint(0, 100)
	print("Result is: " + str(chance))
        if chance in range(0, 5):
            #invoke[2] = invoke[2][:12] + "arglebargle" + invoke[2][12:]
	    invoke[2]  = invoke[2] + '/arglebargle'
            print("Bad URL: " + str(invoke))
            process = subprocess.call(invoke)
        elif chance in range(6, 10):
            invoke[2] += "/fail"
	    print("Server fail: " + str(invoke))
            process = subprocess.call(invoke)
        else:
	    print("Correct: " + str(invoke))
            process = subprocess.call(invoke)
    end = time.time()
    sleep(1-(start-end))
