from flask import Blueprint, request, jsonify 
from app.schemas.pokemon_favorite_schema import PokemonFavoriteSchema 
from marshmallow import ValidationError
from app.models.factory import ModelFactory 
from bson import ObjectId 
from app.tools.response_manager import ResponseManager #importar ResponseManager

RM = ResponseManager() #sustituir jsonify por ResponseManager
bp = Blueprint("pokemon_favorite", __name__, url_prefix="/pokemon_favorite") #ruta de la api
pokemon_favorite_schema = PokemonFavoriteSchema() 
pokemon_favorite_model = ModelFactory.get_model("pokemon_favorites") 

#Create
@bp.route("/create", methods=["POST"]) 
def create():
    try:
        data = pokemon_favorite_schema.load(request.json) 
        pokemon_favorite_id = pokemon_favorite_model.create(data) 
        return RM.succes({pokemon_favorite_id:str(pokemon_favorite_id)}) 

    except ValidationError as err:
        return RM.error("Parametros enviados incorrectos")
    
#Delete
@bp.route("/delete/<string:pokemon_favorite_id>", methods = ["DELETE"]) 
def delete(pokemon_favorite_id):
    pokemon_favorite_model.delete(ObjectId(pokemon_favorite_id)) 
    return RM.success("Yeiii, pokemon eliminado con éxito jiji")

#Get one
@bp.route("/get/<string:user_id>", methods = ["GET"])
def get_pokemon_favorite(user_id):
   pokemon_favorite = pokemon_favorite_model.find_all(ObjectId(user_id))
   return RM.success(pokemon_favorite)

