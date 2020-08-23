from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

userList= {"1": {"name" : "Abdessalam",
                "lastname" : "Zaimi",
                "street": "4 rue Pasteur",
                "city": "Paris",
                "state": "France",
                "zip": 94270,
                "type": "Parent"}}

class Users(Resource):
    def get(self, user_id):
        return userList[user_id]
    
    
api.add_resource(Users, "/user/<string:user_id>")

if __name__ == "__main__":
    app.run(debug=True)
    
