from Test_Section_8.user import User
from Test_Section_8.saveable import Saveable

class Admin(User):
    def __init__(self, username, password, access):
        super(Admin, self).__init__(username, password)
        self.access = access

    def __repr__(self):
        return f'<Admin {self.username}, access{self.access}>'

    def to_dict(self):
        return{
            'username': self.username,
            'password': self.password,
            'access': self.access
        }

