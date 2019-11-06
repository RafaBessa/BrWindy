from flask import Flask, request
from flask_restful import Resource, Api
#from sqlalchemy import create_engine
from json import dumps
from flask_jsonpify import jsonify
from pymongo import MongoClient
#db_connect = create_engine('sqlite:///chinook.db')
app = Flask(__name__)
api = Api(app)
from bson.json_util import dumps
boias = [{"id":"001","Nome":"aaa","Pontos":[(0,1),(2,1)] },{"id":"002","Nome":"bbb","Pontos":[(0,1),(2,1)]} ]

def FirstOrDefault(sequence, id):
    for s in sequence:
        if s["id"] == id:
            return s
    return None


#Retorna o dicionario de uma boia especifica recebendo o nome dela endpoint: /boia/nome
class Boia_id(Resource):
    def get(self, boiaNome):
        client = MongoClient("mongodb+srv://Bessa:vEiz8yoTtgOZzhyC@brwindy-adtf0.mongodb.net/test?retryWrites=true&w=majority")
        db=client.Brwindy
        data = db.Posts2.find({'Name':boiaNome}) 
        return jsonify(dumps(data))

#Retorna todas as boias /boias
class Boias(Resource):
    def get(self):
        client = MongoClient("mongodb+srv://Bessa:vEiz8yoTtgOZzhyC@brwindy-adtf0.mongodb.net/test?retryWrites=true&w=majority")
        db=client.Brwindy
        data = db.Posts2.find()
        blist = []
        for b in data:
            blist.append(dumps(b))
        #return jsonify(data)
        return jsonify(blist)



#Retorna o nome de todas as boias /boiasNomes
class BoiasNome(Resource):
    def get(self):
        client = MongoClient("mongodb+srv://Bessa:vEiz8yoTtgOZzhyC@brwindy-adtf0.mongodb.net/test?retryWrites=true&w=majority")
        db=client.Brwindy
        data = db.Posts2.find({},{'Name':1})
        blist = []
        for b in data:
            blist.append((b['Name']))
        #return jsonify(data)
        return jsonify(blist)

class BoiasAno(Resource):
    def get(self):
        client = MongoClient("mongodb+srv://Bessa:vEiz8yoTtgOZzhyC@brwindy-adtf0.mongodb.net/test?retryWrites=true&w=majority")
        db = client.Brwindy
        data = db.Posts2.find({}, {'Year': 1})
        blist = []
        for b in data:
            blist.append((b['Year']))
        # return jsonify(data)
        return jsonify(blist)


api.add_resource(Boia_id, '/boia/<boiaNome>')
api.add_resource(Boias, '/boias')
api.add_resource(BoiasNome, '/boiasNomes')
api.add_resource(BoiasAno, '/boiasAno')
if __name__ == '__main__':
     app.run(port='5002', debug=True)