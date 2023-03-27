class Shark():

	def __new__(cls, *args):
		if not hasattr(cls, "__instance"):
			print("__new__ is called")
			cls.__instance = super().__new__(cls)
		return cls.__instance
	
	def __init__(self, x, y):
		print("__init__ is called")
		self.size = 2
		self.satiety = 0
		self.x = x
		self.y = y

s1 = Shark(1, 2)
print(s1.x)
print(s1.y)
