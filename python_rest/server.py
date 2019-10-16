from flask import Flask, request
from flask_restful import Resource, Api
#from sqlalchemy import create_engine
from json import dumps
from flask_jsonpify import jsonify

#db_connect = create_engine('sqlite:///chinook.db')
app = Flask(__name__)
api = Api(app)

boias = [{"id":"001","Nome":"aaa","Pontos":[(0,1),(2,1)] },{"id":"002","Nome":"bbb","Pontos":[(0,1),(2,1)]} ]

def FirstOrDefault(sequence, id):
    for s in sequence:
        if s["id"] == id:
            return s
    return None



#Retorna o dicionario de uma boia especifica recebendo o id dela
class Boia_id(Resource):
    def get(self, boiaId):
        result = FirstOrDefault(boias,boiaId)
        print(result)
        return jsonify(result)

#Retorna todas as boias
class Boias(Resource):
    def get(self):
        return jsonify(boias)


api.add_resource(Boia_id, '/boia/<boiaId>')
api.add_resource(Boias, '/boias')

if __name__ == '__main__':
     app.run(port='5002')