#class properties, variable that you think only the class is going to use it
# or to be more organized

class Book:
	Types = ("Hard cover", "PaperCover")
	
	def __init__(self, name, bookType, weight):
		self.name = name 
		self.bookType = bookType
		self.weight = weight
		
	def __repr__(self):
		return f"<name: {self.name}, bookType: {self.bookType}, weight: {self.weight}g>"
	
	@classmethod
	def hardware(cls, name, pageWeight):
		return cls(name, cls.Types[0], pageWeight + 100)
	
	@classmethod
	def papercover(cls, name, pageWeight):
		return cls(name, cls.Types[1], pageWeight)
		
tahaHardware = Book.hardware("lean startup", 200)
tahaPapercover = Book.papercover("zero to ten", 200)

print(tahaHardware)
print(tahaPapercover)
		
	
