from app import mongo 
from app.models.super_clase import SuperClass
from bson import ObjectId

class PokemonFavorites(SuperClass):
    def __init__(self):
        super().__init__("pokemons_favorites")

    def update(self, object_id, data):
        raise NotImplementedError("Los pokemones favoritos no se pueden actualizar")
    
    def find_all(self, user_id):
        data = self.collection.find({"user_id": ObjectId(user_id)})
        for datum in data:
            datum["user_id"]=str(datum["user_id"])
            datum["pokemon_id"]=str(datum["pokemon_id"])
            datum["_id"]=str(datum["_id"])
        return data
    
    def create(self, data):
        data["user_id"] = ObjectId(data["user_id"])
        data["pokemon_id"] = ObjectId(data["pokemon_id"])
        datum = self.collection.insert_ones(data)
        return str(datum.inserted_id)
