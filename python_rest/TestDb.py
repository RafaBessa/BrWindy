from flask import Flask, request
from flask_restful import Resource, Api
#from sqlalchemy import create_engine
from json import dumps
from flask_jsonpify import jsonify
from pymongo import MongoClient
#db_connect = create_engine('sqlite:///chinook.db')
from pprint import pprint
from bson.json_util import dumps



client = MongoClient("mongodb+srv://Bessa:vEiz8yoTtgOZzhyC@brwindy-adtf0.mongodb.net/test?retryWrites=true&w=majority")    
db=client.Brwindy
#data = db.PostsTest.find({'Data.Dado.Date.Year': '2016'},{'Data.Dado.Date.Year':1} )
#data = db.inventory.find({'Data.Dado': {"$elemMatch" : {"Wspd" : "4,237735462" }}})('Data.Dado.' + str(self.eixoX))
data = db.PostsTest.find({},{'Data.Dado.Date.Year':1,'Data.Dado.Pres':1} )
for d in data:
    print(d)
pprint(data)
