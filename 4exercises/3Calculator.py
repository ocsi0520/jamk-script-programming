#!/usr/bin/python3
class Calculator:
	def __init__(self,a):
		self.a=a

	def __add__(self,other):
		return Calculator(self.a+other.a)

	def __mul__(self,other):
		return Calculator(self.a*other.a)

	def __repr__(self):
		return str(self.a)

def main():
	c1 = Calculator(15)
	c2 = Calculator(10)

	print("c1+c2=", c1+c2)
	print("c1*c2=", c1*c2)

if __name__ == "__main__":
	main()