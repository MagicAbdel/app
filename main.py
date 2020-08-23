from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

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

class Users(Resource):
    def get(self, user_id):
        return userList[user_id]
    
    def put(self, user_id):
        args = user_put_args.parse_args()
        if (args["street"] == None or args["city"] == None or args["zip"] == None or args["state"] == None) and args["parent1_id"] == None and args["parent2_id"] == None:
            return {"message" : "provide an address or a parent id"}
        userList[user_id] = args
        return userList[user_id], 201
    
    
api.add_resource(Users, "/user/<string:user_id>")

if __name__ == "__main__":
    app.run(debug=True)
    
