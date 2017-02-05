#!/usr/bin/python3

upperlimit=int(input("upper limit>"))

for i in range(1,upperlimit+1):
	for j in range(1,upperlimit+1):
		print(i,'*',j,'=',i*j)
