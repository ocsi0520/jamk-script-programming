#!/usr/bin/python3

import math

class Triangle:
	def __init__(self, a, b, c):
   		self.a=a
   		self.b=b
   		self.c=c
   		self.gamma=math.acos((a*a+b*b-c*c)/(2*a*b))
   		self.beta=math.acos((a*a-b*b+c*c)/(2*a*c))
   		self.alpha=math.acos((-a*a+b*b+c*c)/(2*b*c))

	def Perimeter(self):
   		return self.a+self.b+self.c

	def Area1(self):
   		s=self.Perimeter()/2
   		return math.sqrt(s*(s-self.a)*(s-self.b)*(s-self.c))

	def Area2(self):
   		return self.c*self.b*math.sin(self.alpha)/2

def main():
	triangle= Triangle(3,4,5)
	print(triangle.Perimeter(),triangle.Area1(),triangle.Area2())

if __name__ == "__main__":
	main()