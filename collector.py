import argparse
import requests
import urllib2
import sys

if(len(sys.argv) > 2):
	#stuff to handle interval.
	print("Hi")

url = sys.argv[1]
results = open("output.tsv", "w")
while True:
	response = urllib2.urlopen(url + "/stats")
	html = response.read()
	print html
	values = html.split("\n")
	del values[-1]
	for stuff in values:
		digit = stuff.split(":")
		results.write(digit[1].strip() + "\t")
	results.write("\n")
