import functools

user = {"username": "bbb", "access_level": "guest"}

def make_function22(access_level_33):
    def decorator22(func):
        @functools.wraps(func)
        def secure_function(*args, **kwargs):
            if user["access_level"] == access_level_33:
                return func(*args, **kwargs)
            else:
                return f"No admin permission  {user['username']}"
        return secure_function
    return decorator22


@make_function22("admin")
def get_admin_password():
        return  "1234"

@make_function22("guest")
def get_dashboard_password():
        return  "user: user_password"

print(get_admin_password.__name__)

print(get_admin_password("admin1"))
print(get_dashboard_password("guest"))
