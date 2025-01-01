
def get_student_info(student_id):
	_ ,student_name, grade = students_map[student_id]
	print(f"{student_name} has a grade of {grade}")

	
students = [
    (101, "Alice", 85),
    (102, "Bob", 90),
    (103, "Charlie", 78),
    (104, "Diana", 92)
]

students_dic = {student[1]: student[2] for student in students}

students_map = {student[0]: student for student in students}
# print(f"students dictionary:\n {students_dic}")
# print(f"students map:\n {students_map}")

student_id = int(input("Enter a Student ID "))
get_student_info(student_id)

