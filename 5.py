#!/usr/bin/env python
# encoding: utf-8
from time import time

start = time()
f = open ('hhga.txt', 'r')
longest = 0
alllines = f.readlines()
f.close()

for line in alllines:
    linelen = len(line.strip())
    if linelen > longest:
        longest = linelen
f.close()
print longest
end = time()
use_time = end - start
print  use_time
