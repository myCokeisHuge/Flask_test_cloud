# package imports
import os
from flask import Flask
from flask_restful import Api
from flask_jwt import JWT


# user created file imports
from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList


app = Flask(__name__)

# Get database url from Heroku environ if run there, else use local sqlite db
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL_NEW', 'sqlite:///data.db')

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'jose'
api = Api(app)

jwt = JWT(app, authenticate, identity)  # /auth

# http://127.0.0.1:5000/item/<name>
api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')  # 'UserRegister' class in user.py


if __name__ == '__main__':  # prevents app from executing if this file is imported into another
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=False)
