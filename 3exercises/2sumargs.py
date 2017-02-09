#!/usr/bin/python3

from sys import argv
sum=0
print("argvs:", argv[1:])
for i in argv[1:]:
	sum+=int(i)
print (sum)
