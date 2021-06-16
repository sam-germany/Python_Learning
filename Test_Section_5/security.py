from user import User


def authenticate22(username, password):
    x = User.find_by_username22(username)
    if x and x.password == password:
        return x

def identity22(payload):
    user_id = payload['identity']
    return User.find_by_id22(user_id)
