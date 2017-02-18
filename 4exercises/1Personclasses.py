#!/usr/bin/python3
class Person:
   def __init__(self, name):
   		self.name=name

   def __eq__(self,other):
   		return self.name == other.name

def main():
	p1 = Person("Bill")
	p2 = Person("Bill")
	p3 = Person("Joe")
	print(p1 == p2)
	print(p3 == p2)

if __name__ == "__main__":
	main()