from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required
from security import authenticate22, identity22

app = Flask(__name__)
app.secret_key = "jose1"
api = Api(app)

jwt = JWT(app, authenticate22, identity22)  # /auth

items = []


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
                        type=float,
                        required=True,
                        help="this field can not be blank .............."
                        )
    data = request.parse_args()
    @jwt_required()
    def get(self, name):
        aa = next(filter(lambda x: x['name'] == name, items), None)
        return {'item': aa}, 200 if aa else 404
    #   return {'item': aa}, 200 if aa is not None else 404


    def post(self, name):
        if next(filter(lambda x: x['name'] == name, items), None) is not None:
            return {'message': "An item with name '{}' already exist".format(name)}, 400

        data22 = Item.parser.parse_args()
        item = {'name': name, 'price': data22['price']}
        items.append(item)
        return item, 201


    def delete(self,name):
        global items
        items = list(filter(lambda x: x['name'] != name, items))
        return {'message': 'Item deleted'}


    def put(self, name):
        data22 = Item.parser.parse_args()

        item33 = next(filter(lambda x: x['name'] == name, items), None)
        if item33 is None:
            item33 = {'name': name, 'price': data22['price']}
            items.append(item33)
        else:
            item33.update(data22)
        return item33


class ItemList(Resource):
    def get(self):
        return {'items': items}


api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')

app.run(port=5000, debug=True)