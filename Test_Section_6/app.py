
from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate22, identity22
from Test_Section_6.resources.user import UserRegister
from Test_Section_6.resources.item import Item, ItemList
from db import db


app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'jose'
api = Api(app)
db.init_app(app)

jwt = JWT(app, authenticate22, identity22)  # /auth     <-- when we call this URI then because of this line it return
                                            #                a Json web tocken
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':                          # vid 84
    app.run(debug=True)  # important to mention debug=True