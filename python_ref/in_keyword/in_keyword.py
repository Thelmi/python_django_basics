
number = 7

user_input = input("Enter 'y' if you would like to play: ")

if user_input in ("y", "Y"):
	user_number = int(input("Guess our number: "))
	if user_input == 7:
		print("Horray")
	elif number - user_number in (1, -1):
		print("you were off by one.")
	else:
		print("OMG")