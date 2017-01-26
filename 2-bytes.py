#!/usr/bin/python3

bytes=int(input("give me many bytes\n"))
bytes/=1024
print ("kilobytes",bytes)
bytes/=1024
print ("megabytes",bytes)
bytes/=1024
print ("gigabytes",bytes)