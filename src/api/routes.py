"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User, Character, Planet, Favorite
from api.utils import generate_sitemap, APIException
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token

api = Blueprint('api', __name__)


# @api.route('/hello', methods=['POST', 'GET'])
# def handle_hello():

#     response_body = {
#         "message": "Hello! I'm a message that came from the backend, check the network tab on the google inspector and you will see the GET request"
#     }

#     return jsonify(response_body), 200

@api.route('/user', methods=['POST'])
def create_user():
    user = User(email=email, password=password)
    db.session.add(user)
    db.session.commit()
    return jsonify(user.serialize())


@api.route('/planet', methods=['GET'])
def get_planet():
    planet_query = Planet.query.all()
    all_serialized_planets = list(map(lambda item:item.serialize(), planet_query))
    return jsonify(all_serialized_planets)



@api.route('/planet', methods=['POST'])
def create_planet():
    name = request.json.get('name', None)
    climate = request.json.get('climate', None)
    rotation_period = request.json.get('rotation_period', None)
    orbital_period = request.json.get('orbital_period', None)
    diameter = request.json.get('diameter', None)
    terrain = request.json.get('terrain', None)
    population = request.json.get('population', None)
    img_url = request.json.get('img_url', None)


@api.route('/character', methods=['GET'])
def get_character():
    character_query = Character.query.all()
    all_serialized_characters = list(map(lambda item:item.serialize(), character_query))
    return jsonify(all_serialized_characters)



@api.route('/favorite', methods=['GET'])
@jwt_required()
def get_favorite():
    current_user_id = get_jwt_identity()
    user = User.query.get(current_user_id)
    if user is None:
        return jsonify({"msg": "User Not Found"}), 403
    favorite_query = Favorite.query.filter_by(user_id=current_user_id)
    all_serialized_favorite = list(map(lambda item:item.serialize(), favorite_query))
    return jsonify(all_serialized_favorite)    
    planet = Planet(name=name,
                    climate=climate,
                    rotation_period=rotation_period,
                    orbital_period=orbital_period,
                    diameter=diameter,
                    terrain=terrain,
                    population=population, 
                    img_url=img_url)
    db.session.add(planet)
    db.session.commit()
    return jsonify(planet.serialize())




@api.route('/token', methods=['POST'])
def create_token():
    if request.json is None:
        return jsonify({"msg":"Missing the payload"}), 400
    email = request.json.get('email', None)
    password = request.json.get('password', None)
    user = User.query.filter_by(email=email, password=password).first()
    if user is None:
        return jsonify({"msg": "Missing email or password"}), 401
    access_token = create_access_token(identity=user.id)
    return jsonify({ "token": access_token, "user_id": user.id })