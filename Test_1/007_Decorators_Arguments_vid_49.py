import functools

user = {"username": "bbb", "access_level": "guest"}

def make_function22(func):
    @functools.wraps(func)
    def secure_function(*args, **kwargs):
        if user["access_level"] == "guest":
            return func(*args, **kwargs)
        else:
            return f"No admin permission  {user['username']}"
    return secure_function

@make_function22
def get_admin_password(a22):
    if a22 == "admin":
        return  "1234"
    elif a22 == "billing":
        return "best password"

print(get_admin_password.__name__)
print(get_admin_password("admin1"))
