from flask import Blueprint, request, jsonify 
from app.schemas.pokemon_favorite_schema import PokemonFavoriteSchema 
from marshmallow import ValidationError
from app.models.factory import ModelFactory 
from bson import ObjectId 
from app.tools.response_manager import ResponseManager #importar ResponseManager
from flask_jwt_extended import jwt_required, get_jwt_identity

RM = ResponseManager() #sustituir jsonify por ResponseManager
bp = Blueprint("pokemon_favorite", __name__, url_prefix="/pokemon_favorite") #ruta de la api
pokemon_favorite_schema = PokemonFavoriteSchema() 
pokemon_favorite_model = ModelFactory.get_model("pokemon_favorites") 

#Create
@bp.route("/create", methods=["POST"]) 
@jwt_required()
def create():
    user_id = get_jwt_identity()
    try:
        data = pokemon_favorite_schema.load(request.json) 
        data["user_id"] = user_id
        pokemon_favorite_id = pokemon_favorite_model.create(data) 
        
        return RM.succes({"_id":str(pokemon_favorite_id)}) 

    except ValidationError as err:
        print(err)
        return RM.error("Parametros enviados incorrectos")
    
#Delete
@bp.route("/delete/<string:pokemon_favorite_id>", methods = ["DELETE"]) 
@jwt_required()
def delete(pokemon_favorite_id):
    pokemon_favorite_model.delete(ObjectId(pokemon_favorite_id)) 
    return RM.success("Pokemon favorito eliminado")

#Get all
@bp.route("/get", methods = ["GET"])
@jwt_required()
def get_pokemon_favorite():
   user_id = get_jwt_identity()
   pokemon_favorite = pokemon_favorite_model.find_all(ObjectId(user_id))
   return RM.success(pokemon_favorite)

