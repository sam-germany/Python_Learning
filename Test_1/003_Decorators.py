user = {"username": "aaa", "access_level": "guest"}

def get_admin_password():
    return "1234"

def make_function(func):
    def secure_function():
        if user["access_level"] == "guest1":
            return func()    # in Decorator we must send with
    return secure_function   # func() with brackets not "func"

x = make_function(get_admin_password)


print(x.__name__)
print(x())
