#!/usr/bin/python3


# W H Y   A G E  ? ? ?

class Student:
   def __init__(self, name, grade):
   		self.name=name
   		self.grade=grade
   	def __repr__(self):
   		return self.name + " " + self.grade

def main():
	student_list = [Student('jim', 4),Student('jane', 3),Student('tim', 5),Student('kim',1),Student('ann',2)]
	print(sorted(student_list,key= lambda x: x.name))
	print(sorted(student_list,key= lambda x: x.grade))

if __name__ == "__main__":
	main()