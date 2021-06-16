from Test_Section_8.admin import Admin
from Test_Section_8.database import Database
from user import User


a = Admin('rolf', '1234', 3)
u = User('jose', 'password')

a.save44()
users = [a, u]
for x in users:
    x.save44()

print(Database.find22(lambda x: x['username'] == 'rolf'))