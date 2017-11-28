import urllib2
import sys
import os.path
from time import sleep

interval = 10.0
outpath = 'output.tsv'
for num, val in enumerate(sys.argv, start=1):
    if num == len(sys.argv):
        break
    if val == '--interval':
        interval = float(sys.argv[num])
    if val == '--path':
        outpath = str(sys.argv[num])


address = sys.argv[1]
# I assume if the file already exists, we want to continue building a log file.
if os.path.isfile(outpath):
    results = open(outpath, 'a')
else:
    results = open(outpath, "w")
address += '/stats'
count = 1
while True:
    response = urllib2.urlopen(address)
    html = response.read()
    line = html.split("\n")
    del line[len(line) - 1]
    for stuff in line:
        digit = stuff.split(":")
        result = digit[1].lstrip()
        results.write(result + "\t")  # grab the value, not the string saying what it is.
    results.write("\n")
    count += 1
    sleep(interval)

