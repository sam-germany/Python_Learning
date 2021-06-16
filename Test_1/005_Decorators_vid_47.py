user = {"username": "aaa", "access_level": "guest"}

def make_function22(func):
    def secure_function():
        if user["access_level"] == "guest":
            return func()
        else:
            return f"No admin permission  {user['username']}"
    return secure_function

@make_function22
def get_admin_password():
    return "1234"


print(get_admin_password.__name__)
print(get_admin_password())
