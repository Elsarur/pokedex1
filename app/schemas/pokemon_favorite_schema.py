from marshmallow import Schema, fields, ValidationError

#Esquema para validar los datos de un pokemon favorito
class PokemonFavoriteSchema(Schema): 
    pokemon_id = fields.Str(
        required = True, 
        validate = lambda x: len(x) > 0,
        error_messages={
            "required": "EL id del pokemon es requerido" 
        }
    )

