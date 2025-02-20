from app import mongo 
from app.models.super_clase import SuperClase
from bson import ObjectId

class PokemonFavorities(SuperClase):
    def __init__(self):
        super().__init__("pokemons_favorites")

    def update(self, object_id, data):
        raise NotImplementedError("Los pokemones favoritos no se pueden actualizar")
    
    
    