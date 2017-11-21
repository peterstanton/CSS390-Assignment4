import argparse
import datetime
#import httplib
import sys
import time
import threading
import os
import subprocess
import random
import numpy


import trafficstats


url = sys.argv[1]
rps = int(sys.argv[2])
jitter = float(sys.argv[3])

lower = rps * (1.0 - jitter)
upper = rps * (1.0 + jitter)

actual = random.randint(lower,upper)

invoke = "curl -G " + url

invoke = invoke.split(" ")

while True:
	start = time.time()
	interval = 1
	for i in range(actual):
		process = subprocess.call(invoke)
