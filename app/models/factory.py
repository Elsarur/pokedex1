from app.models.pokemon_model import Pokemon
from app.models.pokemon_favorite_model import PokemonFavorites
from app.models.users_model import Users

class ModelFactory: #Instancear
    @staticmethod
    def get_model(collection_name):
        models = {
            "users": Users,
            "pokemons": Pokemon,
            "pokemon_favorites": PokemonFavorites
        }

        if collection_name in models:
            return models[collection_name]() #Estamos instanceando la clase 
        raise ValueError(f"Upss, la colección enviado: {collection_name} no existe") #f - concatenar los strings de manera dinamica