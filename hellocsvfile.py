# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 17:26:00 2015

@author: ramku
"""

# Your task is to read the input DATAFILE line by line, and for the first 10 lines (not including the header)
# split each line on "," and then for each line, create a dictionary
# where the key is the header title of the field, and the value is the value of that field in the row.
# The function parse_file should return a list of dictionaries,
# each data line in the file being a single list entry.
# Field names and values should not contain extra whitespace, like spaces or newline characters.
# You can use the Python string method strip() to remove the extra whitespace.
# You have to parse only the first 10 data lines in this exercise,
# so the returned list should have 10 entries!
import os
import csv
import pprint

DATADIR = "/Users/ramku/Documents/Personal/DataScience/Github/Mongodb/"
DATAFILE = "beatles-diskography.csv"


def parse_file(datafile):
    data = []
    print 'parsefile'
    with open(datafile, 'r') as f:
        data = [row for row in csv.reader(f.read().splitlines())]    
        
    return data[1:3]
    

    # a simple test of your implemetation
datafile = os.path.join(DATADIR, DATAFILE)
print datafile
d = parse_file(datafile)

pprint.pprint(d)    

