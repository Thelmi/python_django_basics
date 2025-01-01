
def divide(dividend, divisor=0):
	if divisor != 0:
		return dividend / divisor
	else:
		return "You fool!"
		
result = divide(15, 2) * 5
print(result)