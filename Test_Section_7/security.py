from Test_Section_6.models.usermodel import UserModel


def authenticate22(username, password):
    x = UserModel.find_by_username22(username)
    if x and x.password == password:
        return x

def identity22(payload):
    user_id = payload['identity']
    return UserModel.find_by_id22(user_id)
