#!/usr/bin/env python
# encoding: utf-8

from time import time
start = time()
f = open ('hhga.txt', 'r')
longest = 0
while True:
    linelen = len(f.readline().strip())
    if not linelen:
        break
    if linelen > longest:
        longest = linelen
f.close()
print longest
end = time()
print end - start
