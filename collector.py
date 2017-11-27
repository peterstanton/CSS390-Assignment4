import urllib2
import sys
from time import sleep
import os.path

# Default interval between stats collection is 10 seconds.
interval = 10.0
for num, val in enumerate(sys.argv, start=1):
    if num == len(sys.argv):
        break
    if val == '--interval':
        interval = float(sys.argv[num])
        break

address = sys.argv[1]
# I assume if the file already exists, we want to continue building a log file.
if os.path.isfile('output.tsv'):
    results = open('output.tsv', 'a')
else:
    results = open("output.tsv", "w")
try:
    address += '/stats'
    count = 1
    while True:
        response = urllib2.urlopen(address)
        html = response.read()
        line = html.split("\n")
        del line[len(line) - 1]
        for stuff in line:
            digit = stuff.split(":")
	    digit[1].strip()
	    #print(digit)
            results.write(digit[1] + "\t")
        results.write("\n")
        print('results written for request ' + str(count))
        count += 1
        sleep(interval)
except KeyboardInterrupt:
    print("Ending program...")
    results.write('\n')
    results.close()
    sys.exit()
