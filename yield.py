#!/usr/bin/env python
# encoding: utf-8

def h():
    for i in range(2):
        yield i

c = h()

#for i in range(2):

print c.next()
print c.next()
c.send('hello')
