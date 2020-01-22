class Classify:
    Variable = 2
    def method(self):
        print(self.Variable, self.var)

obj = Classify()
obj.var = 3
obj.method()

print("---- invoke other object/class methods from inside the class. ----")

class Classy:
	def other(self):
		print("other")
	def method(self):
		print("method")
		self.other()


obj = Classy()
obj.method()