from flask import Flask
from flask_restful import Resource, Api
from flask_jwt import JWT, jwt_required
from flask_pymongo import PyMongo


app = Flask(__name__)
app.config['SECRET_KEY'] = 'super-secret'

api = Api(app, prefix="/api/v1")

app.config['MONGO_DBNAME'] = 'restDB'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/restDB'

mongo = PyMongo(app)


class User(object):
	def __init__(self, id):
		self.id = id

	def __str__(self):

		return "User(id='%s')" % self.id


def verify(username, password):
	#userDetails()
	users = mongo.db.users
	#print users
	USER_DATA = {user['username']:user['password'] for user in users.find()}
	if not (username and password):
		return False
	if(USER_DATA.get(username) == password):
		userId = users.find_one({'username':username})
		
		return User(id = userId['_id'])


def identity(payload):
	user_id = payload['identity']
	return {"user_id": user_id}

jwt = JWT(app, verify, identity)


class PrivateResource(Resource):
    @jwt_required()
    def get(self):
        return {"meaning_of_life": 42}


api.add_resource(PrivateResource, '/private')

if __name__ == '__main__':
    app.run(debug=True)