import functools
user = {"username": "jose", "access_level": "guest"}

def secure_get_admin(func):
	@functools.wraps
	def secure_function():
		if user['access_level'] == "admin":
			return func()
		else:
			return f"No admin permissions for {user['username']}"
	return secure_function

@secure_get_admin
def get_admin_password():
	return "1234"

print(get_admin_password.__name__) 