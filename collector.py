import urllib2
import sys
from time import sleep
import os.path

#Default interval between stats collection is 10 seconds.
interval = 10
for i in sys.argv:
    if sys.argv[i] == '--interval':
        interval = sys.argv[i+1]
        break

url = sys.argv[1]
#I assume if the file already exists, we want to continue building a log file.
if os.path.isfile(url):
    results = open('output.txv', 'a')
else:
    results = open("output.tsv", "w")
try:
    while True:
        response = urllib2.urlopen(url + "/stats")
        html = response.read()
        print html
        line = html.split("\n")
        del line[-1]
        for stuff in line:
            digit = stuff.split(":")
            results.write(digit[1].strip() + "\t")
        results.write("\n")
        sleep(interval)
except KeyboardInterrupt:
    print("Ending program...")
    results.close()
    sys.exit()

