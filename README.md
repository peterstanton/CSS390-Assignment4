# CSS390-Assignment4

This assignment involves periodically querying a website as to its status, parsing the response
and compiling the data into a tab-separated output file and graph of the website status over time.

## Installation

This program is written for Python 2.7, and gnuplot 4.6 patchlevel 6.

## Usage

1. To use this program, first invoke the Timeserver program on local machine.

2. Then invoke Trafficgen to simulate a load on that url.

3. Next invoke Collector on the server to periodically sample the server statistics. By default, it samples every 10
seconds, but the --interval flag can be used to set the interval manually.

4. When enough data has been gathered to your satisfaction, invoke the plotting script with ./plot.sh to generate
a plot of the data.

## Assumptions

1. If an output.tsv already exists from a previous run, in invoking Collector again, the user most likely wishes to add
to previously collected data, and the log should be appended to, not overwritten.


## Known Bugs

* Because time on the x-axis is measured in Unix time, seconds since 1970, the x-axis labeling is very crowded.

* The server occasionally becomes congested with requests with high rps, making it difficult to log all the reports
properly.

* Sometimes after completing a high number of requests per second, it improperly sleeps when it should immediately
continue.

* Because of limitations with the implementation of random.randint, I have to force the results of the jitter
computation to integers because the random number function, random.randrange() requires integer parameters.

## Credits

TODO: Write credits

* https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet

* https://unix.stackexchange.com/questions/34440/automate-gnuplot-plotting-with-bash

* https://people.duke.edu/~hpgavin/gnuplot.html

* Thanks to Cameron Padua for helping me figure out how to parse responses from the server for Collector.py, and
pointing out that I need to be deleting whitespace that was throwing off my parsing.

* http://lowrank.net/gnuplot/datafile2-e.html

* http://gnuplot.sourceforge.net/demo/simple.html