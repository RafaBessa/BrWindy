from flask import Flask, request
from flask_restful import Resource, Api
#from sqlalchemy import create_engine
#from json import dumps
from flask_jsonpify import jsonify
from pymongo import MongoClient
from bson.json_util import dumps
import BuilderQuery as bq

app = Flask(__name__)
api = Api(app)





#Retorna o dicionario de uma boia especifica recebendo o nome dela endpoint: /boia/nome
class Boia_id(Resource):
    def get(self, boiaNome):
        client = MongoClient("mongodb+srv://Bessa:vEiz8yoTtgOZzhyC@brwindy-adtf0.mongodb.net/test?retryWrites=true&w=majority")    
        db=client.Brwindy
        data = db.PostsTest.find({'Name':boiaNome}) 
        return jsonify(dumps(data))

#Retorna todas as boias /boias
class Boias(Resource):
    def get(self):
        client = MongoClient("mongodb+srv://Bessa:vEiz8yoTtgOZzhyC@brwindy-adtf0.mongodb.net/test?retryWrites=true&w=majority")    
        db=client.Brwindy
        data = db.PostsTest.find() 
        blist = []
        for b in data:
            blist.append(dumps(b))
      
        return jsonify(blist)



#Retorna o nome de todas as boias /boiasNomes
class BoiasNome(Resource):
    def get(self):
        client = MongoClient("mongodb+srv://Bessa:vEiz8yoTtgOZzhyC@brwindy-adtf0.mongodb.net/test?retryWrites=true&w=majority")    
        db=client.Brwindy
        data = db.PostsTest.find({},{'Name':1}) 
        blist = []
        for b in data:
            blist.append((b['Name']))
     
        return jsonify(blist)



class BoiasAnos(Resource):
    def get(self):
        client = MongoClient("mongodb+srv://Bessa:vEiz8yoTtgOZzhyC@brwindy-adtf0.mongodb.net/test?retryWrites=true&w=majority")    
        db=client.Brwindy
        data = db.PostsTest.distinct('Data.Dado.Date.Year')#gets the unique values of year
        print(data)
        return jsonify(data)
      

class BoiasCat(Resource):
    def get(self):
        return jsonify(  ['# Epoca',
        'Date.Year',
        'Date.Month',
        'Date.Day', 
        'Date.Hour',
        'Date.Minute',
        'Location.Lat',
        'Location.Lon',
        'Wspd',
        'Wspdflag',
        'Wdir',
        'Gust',
        'Atmp',
        'Pres',
        'Dewp',
        'Humi',
        'Arad',
        'Wtmp',
        'Wvht',
        'Wmax',
        'Dpd',
        'Mwd',
        'Spred'])


class Boiasquery(Resource):
    def get(self,Nome,Ano,X,Y):
        valores = {
                'Nome' : Nome,
                'Ano' : Ano,
                'eixoX' : X,
                'eixoY' : Y
                }           
        
        director = bq.Director()
        builder = bq.ConcreteBuilder1()
        director.builder = builder
        
        return director.build_full_featured_query(valores)


class BoiasqueryMinMax(Resource):
    def get(self,Nome,Ano,X,Y,minX,maxX,minY,maxY):
        valores = {
                'Nome' : Nome,
                'Ano' : Ano,
                'eixoX' : X,
                'eixoY' : Y,
                'minX' : minX,
                'minY' : minY,
                'maxX' : maxX,
                'maxY' : maxY,
                }           
                
        director = bq.DirectorMaxmin()
        builder = bq.ConcreteBuilderMaxMin()
    
        director.builder = builder
        
        return director.build_full_featured_query(valores)

api.add_resource(BoiasqueryMinMax, '/boiasQueryMinMax/<Nome>/<Ano>/<X>/<Y>/<minX>/<maxX>/<minY>/<maxY>') 
api.add_resource(Boiasquery, '/boiasQuery/<Nome>/<Ano>/<X>/<Y>') 
api.add_resource(BoiasCat, '/boiasCat') 
api.add_resource(BoiasAnos, '/boiasAno') 
api.add_resource(Boia_id, '/boia/<boiaNome>')
api.add_resource(Boias, '/boias')
api.add_resource(BoiasNome, '/boiasNomes')
if __name__ == '__main__':
     app.run(port='5002', debug=True)