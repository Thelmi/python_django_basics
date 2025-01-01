from operator import itemgetter

def search(sequence, expected, finder):
	for elem in sequence:
		if finder(elem) == expected:
			return elem
	raise RuntimeError(f"Could not find and element with {expected}.")

friends = [
	{"name": "Rolf Smith", "age": 24},
	{"name": "Adam Woo;", "age": 40},
	{"name": "Adam Wood", "age": 27}
]

def get_friend_name(friend):
	return friend["name"]

print(search(friends, "Rolf Smith", itemgetter("name")))