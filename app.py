# -*- coding: utf-8 -*-
from flask import Flask, jsonify, request
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'database'
app.config['MONGO_URI'] = 'mongodb+srv://root:toor@cluster0.phi3r.mongodb.net/database?retryWrites=true&w=majority'

mongo = PyMongo(app)

@app.route('/')
def index():
    user = mongo.db.user
    user_id = user.insert({'name' : name,'lastname' : lastname,'street' : street, 'city' : city, 'zipcode' : zipcode, 'state' : state, 'parent1_id' : parent1_id, 'parent2_id' : parent2_id})
    

@app.route('/user', methods=['GET'])
def get_all_users():
    user = mongo.db.user

    output = []

    for q in user.find():
        output.append({'name' : q['name'],'lastname' : q['lastname'],'street' : q['street'], 'city' : q['city'], 'zipcode' : q['zipcode'], 'state' : q['state'], 'parent1_id' : q['parent1_id'], 'parent2_id' : q['parent2_id']})

    return jsonify({'result' : output})

@app.route('/user/<id>', methods=['GET'])
def get_one_user(name, lastname):
    user = mongo.db.user

    q = user.find_one({'id' : id})

    if q:
        output = {'name' : q['name'],'lastname' : q['lastname'],'street' : q['street'], 'city' : q['city'], 'zipcode' : q['zipcode'], 'state' : q['state'], 'parent1_id' : q['parent1_id'], 'parent2_id' : q['parent2_id']}
    else:
        output = 'No results found'

    return jsonify({'result' : output})

@app.route('/user', methods=['POST'])
def add_user():
    user = mongo.db.user 

    name = request.json['name']
    lastname = request.json['lastname']
    street = request.json['street']
    city = request.json['city']
    zipcode = request.json['zipcode']
    state = request.json['state']
    parent1_id = request.json['parent1_id']
    parent2_id = request.json['parent2_id']


    user_id = user.insert({'name' : name,'lastname' : lastname,'street' : street, 'city' : city, 'zipcode' : zipcode, 'state' : state, 'parent1_id' : parent1_id, 'parent2_id' : parent2_id})
    new_user = user.find_one({'_id' : user_id})

    output = {'name' : new_user['name'],'lastname' : new_user['lastname'],'street' : new_user['street'], 'city' : new_user['city'], 'zipcode' : new_user['zipcode'], 'state' : new_user['state'], 'parent1_id' : new_user['parent1_id'], 'parent2_id' : new_user['parent2_id']}

    return jsonify({'result' : output})

if __name__ == '__main__':
    app.run(debug=True)