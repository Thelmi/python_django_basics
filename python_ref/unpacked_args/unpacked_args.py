def multiply(*args):
	total = 1
	for arg in args:
		total = total * arg
	return (total)

def apply(*args, operator):
	if operator == "*":
		return multiply(*args)
	elif operator == "+":
		return sum(args)
	else:
		"Not a valid operator"

print(apply(1 , 3 , 4, 7, operator="*"))