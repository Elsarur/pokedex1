from flask import Blueprint, request  
from marshmallow import ValidationError
from app.models.factory import ModelFactory 
from bson import ObjectId 
from app.tools.response_manager import ResponseManager

RM = ResponseManager()
bp = Blueprint("pokemon", __name__, url_prefix="/pokemons")
pokemon_model = ModelFactory.get_model("pokemons")

#Create

@bp.route("/create", methods=["POST"]) #
def create():
    try:
        data = request.json
        pokemon_id = pokemon_model.create(data)  
        return RM.success({pokemon_id:str(pokemon_id)}), 200 

    except ValidationError as err:
        return RM.error("Los parametros son incorrectos"), 400

#Delete

@bp.route("/delete/<string:pokemon_id>", methods = ["DELETE"]) 
def delete(pokemon_id):
    pokemon_model.delete(ObjectId(pokemon_id)) 
    return RM.success("Pokemon eliminado con exito"), 200

#Get one

@bp.route("/get/<string:pokemon_id>", methods = ["GET"])
def get_pokemon(pokemon_id):
    pokemon = pokemon_model.find_by_id(ObjectId(pokemon_id))
    return RM.success(pokemon), 200

#Get all

@bp.route("/get/<string:pokemon_id>", methods = ["GET"])
def get_pokemon(pokemon_id):
   pokemon = pokemon_model.find_all(ObjectId(pokemon_id))
   return RM.success(pokemon)

