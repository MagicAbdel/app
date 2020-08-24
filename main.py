from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class UserModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    lastname = db.Column(db.String(100), nullable=False)
    street = db.Column(db.String(100))
    city = db.Column(db.String(100))
    zipcode = db.Column(db.Integer)
    state = db.Column(db.String(100))
    parent1_id = db.Column(db.Integer)
    parent2_id = db.Column(db.Integer)
    
    def __init__(self, name, lastname, street, city, zipcode, state, parent1_id, parent2_id):
      self.name = name
      self.lastname = lastname
      self.street = street
      self.city = city
      self.zipcode = zipcode
      self.state = state
      self.parent1_id = parent1_id
      self.parent2_id = parent2_id
    

user_put_args = reqparse.RequestParser()
user_put_args.add_argument("name", type=str, help="Please specify the name of the user")
user_put_args.add_argument("lastname", type=str, help="Please specify the last name of the user")
user_put_args.add_argument("street", type=str, help="Street")
user_put_args.add_argument("city", type=str, help="City")
user_put_args.add_argument("zipcode", type=int, help="zipcode")
user_put_args.add_argument("state", type=str, help="State")
user_put_args.add_argument("parent1_id", type=int, help="Id of the first parent")
user_put_args.add_argument("parent2_id", type=int, help="Id of the second parent")

user_update_args = reqparse.RequestParser()
user_update_args.add_argument("name", type=str, help="Please specify the name of the user")
user_update_args.add_argument("lastname", type=str, help="Please specify the last name of the user")
user_update_args.add_argument("street", type=str, help="Street")
user_update_args.add_argument("city", type=str, help="City")
user_update_args.add_argument("zipcode", type=int, help="zipcode")
user_update_args.add_argument("state", type=str, help="State")
user_update_args.add_argument("parent1_id", type=int, help="Id of the first parent")
user_update_args.add_argument("parent2_id", type=int, help="Id of the second parent")

data_fields = {
    'id' : fields.Integer,
    'name' : fields.String,
    'lastname' : fields.String,
    'street' : fields.String,
    'city' : fields.String,
    'zipcode' : fields.String,
    'state' : fields.String,
    'parent1_id' : fields.Integer,
    'parent2_id' : fields.Integer
}

class Users(Resource):
    @marshal_with (data_fields)
    def get(self, user_id):
        result = UserModel.query.get(user_id)
        if result is None:
            abort(400, messge="user id not found")
        return result
        
    
    @marshal_with (data_fields)
    def put(self, user_id):
        result = UserModel.query.get(user_id)
        if result:
            abort(409, message="user id taken")
        
        args = user_put_args.parse_args()
        if (args["street"] == None or args["city"] == None or args["zipcode"] == None or args["state"] == None) and args["parent1_id"] == None and args["parent2_id"] == None:
            abort(400, message="Please provide correct information")
        
        new_user = UserModel(args["name"], args["lastname"], street=args["street"], city=args["city"], zipcode=args["zipcode"], state=args["state"], parent1_id=args["parent1_id"], parent2_id=args["parent2_id"])
        db.session.add(new_user)
        db.session.commit()
        return new_user, 201
    
    def patch(self, video_id):
        args = user_put_args.parse_args()
    
    def delete(self, user_id):
        del userList[user_id]
        return '', 204
        
    
api.add_resource(Users, "/user/<string:user_id>")

if __name__ == "__main__":
    app.run(debug=True)
    
