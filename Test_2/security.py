from user import User

users = [
      User(1, 'bob', 'asdf')
]

"""
username_mapping = { 'bob':  {
                              'id': 1,
                              'username': 'bob',
                              'password': 'asdf'
}}

userid_mapping = { 1:  {
                          'id': 1,
                          'username': 'bob',
                          'password': 'asdf'
}}
"""
# here below two lines are the short cut of the above   "username_mapping"   and     "userid_mapping"

username_mapping = { u.username: u for u in users}
userid_mapping = {u.id: u for u in users}

def authenticate22(username, password):
    x = username_mapping.get(username, None)
    if x and x.password == password:
        return x

def identity22(payload):
    user_id = payload['identity']
    return userid_mapping.get(user_id, None)

