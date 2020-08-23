from flask import Flask
from flask_restful import Api, Resource, reqparse, abort
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

db = SQLAlchemy(app)

class UserModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    lastname = db.Column(db.String(100), nullable=False)
    street = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(100), nullable=False)
    zipcode = db.Column(db.Integer, nullable=False)
    state = db.Column(db.String(100), nullable=False)
    parent1_id = db.Column(db.Integer)
    parent2_id = db.Column(db.Integer)
    
db.create_all()

userList= {"0": {"name" : "Abdessalam",
                "lastname" : "Zaimi",
                "street": "4 rue Pasteur",
                "city": "Paris",
                "zip": 94270,
                "state": "France",
                "parent1_id": 0,
                "parent2_id": 0}}

user_put_args = reqparse.RequestParser()
user_put_args.add_argument("name", type=str, help="Please specify the name of the user", required = True)
user_put_args.add_argument("lastname", type=str, help="Please specify the last name of the user", required = True)
user_put_args.add_argument("street", type=str, help="Street")
user_put_args.add_argument("city", type=str, help="City")
user_put_args.add_argument("zip", type=int, help="zipcode")
user_put_args.add_argument("state", type=str, help="State")
user_put_args.add_argument("parent1_id", type=int, help="Id of the first parent")
user_put_args.add_argument("parent2_id", type=int, help="Id of the second parent")

def check_exist(user_id, boolean):
    if boolean == False:
        if user_id not in userList:
            abort(404, message="User id is not valid")
    else:
        if user_id in userList:
            abort(409, message="User id already exists")

class Users(Resource):
    def get(self, user_id):
        check_exist(user_id, False)
        return userList[user_id]
    
    def put(self, user_id):
        check_exist(user_id, True)
        args = user_put_args.parse_args()
        if (args["street"] == None or args["city"] == None or args["zip"] == None or args["state"] == None) and args["parent1_id"] == None and args["parent2_id"] == None:
            abort(400, message="Please provide an address or a parent id")
        
        userList[user_id] = args
        return userList[user_id], 201
    
    def delete(self, user_id):
        check_exist(user_id, False)
        del userList[user_id]
        return '', 204
        
    
api.add_resource(Users, "/user/<string:user_id>")

if __name__ == "__main__":
    app.run(debug=True)
    
