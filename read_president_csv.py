#!/usr/bin/env python
import csv

with open('DATA/presidents.csv') as pres_in:
    rdr = csv.reader(pres_in)
    for row in rdr:
        print(row)

