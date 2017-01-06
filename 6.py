#!/usr/bin/env python
# encoding: utf-8
from time import time

start = time()
f = open ('hhga.txt', 'r')
alllinelens = [len(x.strip()) for x in f]
f.close()
end = time()
print max(alllinelens)
use_time = end - start
print  use_time
