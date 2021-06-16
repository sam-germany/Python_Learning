user = {"username": "aaa", "access_level": "guest"}

def get_admin_password():
    return "1234"

def make_function(func):
    def secure_function():
        if user["access_level"] == "guest1":
            return func()
        else:
            return f"No admin permission  {user['username']}"
    return secure_function

x = make_function(get_admin_password)

print(x.__name__)
print(x())
