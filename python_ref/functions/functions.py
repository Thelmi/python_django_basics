
def add_friend():
	friend_name = input("Enter your new friend name ")
	friends_list = friends + [friend_name]
	print(friends_list)

friends = ["Rolf", "Bob"]

add_friend()


print(friends)