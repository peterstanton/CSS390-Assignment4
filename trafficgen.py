import argparse
import datetime
#import httplib
import sys
import time
import threading
import os
import subprocess


import trafficstats


url = sys.argv[1]
rps = sys.argv[2]
jitter = sys.argv[3]

#lower = rps * (1.0 - jitter)
#upper = rps * (1.0 + jitter)

#actual = random.randint/uniform(lower,upper)

bashCommand = "curl -G " + url

bashCommand = bashCommand.split(" ")


interval = 1/rps
while True:
	startTime = time()
	process = subprocess.call(bashCommand)
	endTime = 
