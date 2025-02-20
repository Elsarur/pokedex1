#sustituir jsonify por ResponseManager

from flask import jsonify

class ResponseManager:
    def success(self, data):
        if type(data) == "str":
            data = {
                "message": data
            }
        return jsonify(data), 200
    
    def error(self, data="Invalid request"):
        if type(data) == "str":
            data = {
                "message": data
            }
        return jsonify(data), 400
    

    def error_server(self, data="SERVER ERROR"): 
        if type(data) == "str":
            data = {
                "message": data
            }
        return jsonify(data), 500
    