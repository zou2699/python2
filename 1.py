#!/usr/bin/python
#coding:utf8

Tn = 0
Sn = []
n = int(raw_input('n = \n'))
a = int(raw_input('a = \n'))
for counter in range(n):
	Tn = Tn + a
	a = a * 10
	Sn.append(Tn)
print Sn

