from app import mongo

class SuperClass:
    def _init_(self, collection): #Creamos el constructor
        self.collection = mongo.db[collection] #Pasar la conexión de manera dinámica

#Los metodos ya no pueden ser staticos
#De la clase estoy abstrayendo 

    def find_all(self):
        data = self.collection.find() 
        return list(data) 

    def find_by_id(self, object_id):
        datum = self.collection.find_one({ 
            "_id": object_id
        }) 
        return datum
    
    def create(self, data): 
        datum = self.collection.insert_one(data)
        return str(datum.inserted_id) 
    
    def update(self, object_id, data): #Metodo para guardar el pokemonn
        datum = self.collection.update_one({
            "_id": object_id
        },{
            "$set": data 
        })
        return datum
    
    def delete(self, object_id): #Metodo para eliminar el pokemon
        return self.collection.delete_one({"_id": object_id})

    

    #Dos colecciones una de usuarios y otra de pokemones, pokemones favoritos