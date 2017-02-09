#!/usr/bin/python3

from sys import argv
sum=0
print("argvs:", argv[1:])

j=0
for i in argv[1:]:
    try:
        sum+=int(i)
        j+=1
    except Exception as e:
        pass
print (sum,sum/j)
