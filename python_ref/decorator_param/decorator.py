
import functools

user = {"username": "alice", "role": "guest"}

def role_required(allow_rules):
	def decorator(func):
		def security_check(*args, **kwargs):
			if user["role"] in allow_rules:
					return func(*args, *kwargs)
			return "You don't have an access"
		return security_check
	return decorator

@role_required(["admin"])
def view_admin_dashboard():
    return "Welcome to the admin dashboard."

@role_required(["admin", "manager"])
def view_manager_report():
    return "Here's the manager's report."

print(view_admin_dashboard())       # Output: No access for alice
print(view_manager_report())        # Output: No access for alice

# Change the user's role to "manager"
user = {"username": "bob", "role": "manager"}
print(view_admin_dashboard())       # Output: No access for bob
print(view_manager_report())        # Output: Here's the manager's report
