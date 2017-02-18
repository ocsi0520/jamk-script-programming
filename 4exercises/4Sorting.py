#!/usr/bin/python3
class Person:
   def __init__(self, name):
   		self.name=name

   def __eq__(self,other):
   		return self.name == other.name

class Worker (Person):
	_contract_types = ["FullTime","PartTime","Hourly"]

	def __init__(self, name,contract_type,salary):
   		super().__init__(name)
   		self.contract_type=contract_type
   		self.salary=salary
   		if contract_type not in Worker._contract_types:
   			raise Exception("Dunno what tu du")

	def __repr__(self):
   		return self.name + " " + self.contract_type + " " +  str(self.salary)


def main():
	persons = list()
	persons.append(Worker("Bill","FullTime", 4500))
	persons.append(Worker("John","PartTime", 2900))
	persons.append(Worker("Calle","FullTime", 3900))
	persons.append(Worker("Mary","Hourly", 2600))
	persons.append(Worker("Jill","FullTime", 4100))
	persons.append(Worker("Ann","Hourly", 3300))
	print(sorted(persons,key=lambda x: x.salary))
	print(sorted(persons,key=lambda x: x.name))

if __name__ == "__main__":
	main()

