class Class:
	Var = 1
	def __init__(self,val):
#		self.Var = val  # instance variable
		Class.Var = val # class variable => the __dict__ of the object is empty

print(Class.__dict__)
object = Class(2)
print(Class.__dict__)
print(object.__dict__)