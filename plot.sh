#!/usr/bin/env bash
gnuplot <<- EOF
	set title "Time server status over time"
	set xlabel "Unix Time"
	set ylabel "Total count of code responses"
	set autoscale
	set term png
	set output "result.png"
	plot 'output.tsv' using 1:2 title '200s' with lines,\
	'output.tsv' using 1:3 title '400s' with lines,\
	'output.tsv' using 1:4 title '500s' with lines
EOF

