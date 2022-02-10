"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User, Character, Planet, Favorite
from api.utils import generate_sitemap, APIException

api = Blueprint('api', __name__)


@api.route('/hello', methods=['POST', 'GET'])
def handle_hello():

    response_body = {
        "message": "Hello! I'm a message that came from the backend, check the network tab on the google inspector and you will see the GET request"
    }

    return jsonify(response_body), 200


@api.route('/user', methods=['GET'])
def create_user():
    user = User(email="my_super@email.com", password="my_super@email.com", gender="male")
    db.session.add(user)
    db.session.commit()
    return jsonify(user.serialize())



@api.route('/planets', methods=['GET'])
def create_planet():
    planet = Planet(name="name", climate="climate", rotation_period="rotation_period", orbital_period="orbital_period", diameter="diameter", terrain="terrain", population="population")
    db.session.add(planet)
    db.session.commit()
    return jsonify(planet.serialize())



@app.route("/token", methods=["POST"])
def create_token():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    # Query your database for username and password
    user = User.query.filter_by(username=username, password=password).first()
    if user is None:
        # the user was not found on the database
        return jsonify({"msg": "User not found"}), 401
    
    return jsonify(character.serialize())




@api.route('/characters', methods=['GET'])
def create_character():
    character_query = Character.query.all()
    all_serialized_characters = list(map(lambda item: item.serialize(), character_query))
    return jsonify(character.serialize())