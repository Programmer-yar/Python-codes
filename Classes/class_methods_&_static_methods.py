class Employee:
	# class variables
	num_of_emps = 0
	raise_amt = 1.04

	def __init__(self, first, last, pay):
		# class attributes
		self.first =  first
		self.last = last
		self.email = first + '.' + last + '@email.com'
		self.pay = pay

		Employee.num_of_emps += 1

	def fullname(self):
		return f'{self.first} {self.last}'

	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amt)

	# Class Methods
	@classmethod
	def set_raise_amt(cls, amount):
		"""
		Class Methods take 'class' -> 'cls' as argument as compared to 
		regular methods which takes 'instance' -> 'self' as argument 
		"""
		cls.raise_amt = amount

	@classmethod
	def from_string(cls, emp_str):
		""" Using class Mehthos as alternative constructor """
		first, last, pay = emp_str_1.split('-')
		return cls(first, last, pay)



emp_1 = Employee('Corey', 'Schafer', '40000')
emp_2 = Employee('Ahmad', 'Yar', '20000')

Employee.set_raise_amt(1.1)

print(Employee.raise_amt)
print('Total number of Employees: ', Employee.num_of_emps)
print(emp_1.raise_amt)
print(emp_2.raise_amt)



emp_str_1 = 'abdul-haseeb-10000'
emp_str_2 = 'zubaid-ramay-5000'
emp_str_3 = 'usman-yaqoob-20000'

""" below constructor is shifted to class method """
# first, last, pay = emp_str_1.split('-')
# new_emp_1 = Employee(first, last, pay)

new_emp_1 = Employee.from_string(emp_str_1)

print(f'pay: {new_emp_1.pay}, email:{new_emp_1.email}')