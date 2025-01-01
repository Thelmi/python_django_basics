
class Student:
	def __init__(self, name, grades):
		self.name = name
		self.grades = grades
	def average(self):
		return sum(self.grades) / len(self.grades)
		
		

student1 = Student("Taha", (89,  90, 93, 78, 90))
student2 = Student("Maaz", (88,  91, 90, 80, 86))

print(f"student1 name: {student1.name}")
print(f"student1 grades: {student1.grades}")
print(f"student1 average:  {student1.average()}")
print(f"student2 name: {student2.name}")
print(f"student2 grades: {student2.grades}")
print(f"student2 average:  {student2.average()}")
