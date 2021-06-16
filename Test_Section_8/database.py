class Database:
    content = {'users': []}

    @classmethod
    def insert22(cls, data):
        cls.content['users'].append(data)

    @classmethod
    def remove(cls, finder):
        cls.content['users'] = [x for x in cls.content['users'] if not finder(x)]

    @classmethod
    def find22(cls, finder):
        return [x for x in cls.content['users'] if finder(x)]


#  print(Database.find22(lambda x: x['username'] == 'rolf'))