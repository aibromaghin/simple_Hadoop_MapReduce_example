#!/usr/bin/env python
import sys

# create set of stopwords 
stops = set(['i', 'the', 'and', ',', '.', ';', '?', '!', 'a', 'me', 'my', 'you', 'your', 'are', 'be', 'to', 'or', 'but', 'he', 'her', 'his', 'hers', 'with', 'for', 'by'])

# get all lines from stdin
for line in sys.stdin:
    # remove leading and trailing whitespace and convert to lowercase
    line = line.strip().lower()

    # split the line into words; splits on any whitespace
    words = line.split()

    # output tuples (word, 1) in tab-delimited format after removing stopwords
    for word in words:
	if word not in stops:
             print '%s\t%s' % (word, "1")
