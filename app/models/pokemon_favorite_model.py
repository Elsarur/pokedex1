from app import mongo
from app.models.super_class import SuperClass
from bson import ObjectId

#creamos la clase pokemon
class PokemonFavorites(SuperClass):
    def __init__(self):
        super().__init__("pokemons")

    def create(self, data):
        raise NotImplementedError("Los pokemones no se pueden crear")
    
    def delete(self, object_id):
        raise NotImplementedError("Los pokemones no se pueden eliminar")
    
    def update(self, object_id, data):
        raise NotImplementedError("Los pokemones no se pueden actualizar")
    
    def find_all(self, user_id):
         data = list(self.collection.find({"user_id": ObjectId(user_id)}))
         for datum in data:
          datum["user_id"] = str(datum["user_id"])
          datum["pokemon_id"] = str(datum["pokemon_id"])
          datum["_id"] = str(datum["_id"])

         return data
    
    def create(self, data):
     data["user_id"] = ObjectId(data["user_id"])
     data["pokemon_id"] = ObjectId(data["pokemon_id"])
     datum = self.collection.insert_one(data)
     return str(datum.inserted_id)