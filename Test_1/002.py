user = {"username": "aaa", "access_level":"guest"}

def get_admin_password():
    return "1234"

def secure_function(func):
    if user["access_level"] == "guest":
        return func

x = secure_function(get_admin_password)


print(x.__name__)
print(x())