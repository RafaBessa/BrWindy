import csv
from pymongo import MongoClient
#from pprint import pprint
import pprint
import os
from copy import deepcopy

class Boia:
    def __init__(self):
        self.Boia = deepcopy({
        'Name':"",
        'Data':[ ],
            })
    
    
class Data:
    def __init__(self):
        self.dat = deepcopy({
            'Dado' : {
                '# Epoca':'',
                'Date':{'Year':'', 'Month':'','Day':'', 'Hour':'','Minute':''}, 
                'Location':{'Lat':'', 'Lon':''},
                'Wspd':'',
                'Wspdflag':'',
                'Wdir': '',
                'Gust':'',
                'Atmp':'',  
                'Pres':'',
                'Dewp':'',
                'Humi':'',
                'Arad':'',
                'Wtmp':'',
                'Wvht':'',
                'Wmax':'',
                'Dpd':'',
                'Mwd':'',
                'Spred':''
                }
            })
   




def CsvToDict(pathArquivo,NomeBoia):
    arquivo = open(pathArquivo)

    dados = csv.DictReader(arquivo)


    #i=0

            #  Dado = { '# Epoca':'',
            # 'Date':{}, 
            # 'Location':{},
            # 'Battery':'',
            # 'bHead':'',
            # 'Wspd':'',
            # 'Wspdflag':'',
            # 'Wdir': '',
            # 'Gust':'',
            # 'Atmp':'',  
            # 'Pres':'',
            # 'Dewp':'',
            # 'Humi':'',
            # 'Arad':'',
            # 'Wtmp':'',
            # 'Cvel1':'',
            # 'Cdir1':'',
            # 'Cvel2':'',
            # 'Cdir2':'',
            # 'Cvel3':'',
            # 'Cdir3':'',
            # 'Wvht':'',
            # 'Wmax':'',
            # 'Dpd':'',
            # 'Mwd':'',
            # 'Spred':''
            # }

    NomeDosDados = ['# Epoca','Wspd','Wspdflag','Wdir','Gust','Atmp', 
                    'Pres','Dewp','Humi','Arad','Wtmp','Wvht','Wmax','Dpd','Mwd','Spred']
    #transformar o csv em dict

    #instaciar uma nova boia
    Doc = Boia()
    Doc.Boia['Name'] = NomeBoia
    for d in dados:
        tupla = Data()
                     
        #Pegar a Data
        if(d['Year'].replace('.0','') != '2016' ):
            continue
        tupla.dat['Dado']['Date']['Year'] = d['Year'].replace('.0','')
        tupla.dat['Dado']['Date']['Month'] = d['Month'].replace('.0','')
        tupla.dat['Dado']['Date']['Day'] = d['Day'].replace('.0','')
        tupla.dat['Dado']['Date']['Hour'] = d['Hour'].replace('.0','')
        tupla.dat['Dado']['Date']['Minute'] = d['Minute'].replace('.0','')
        
        #Pegar localizacao Lat':'', 'Lon'

        tupla.dat['Dado']['Location']['Lat'] = d['Lat']
        tupla.dat['Dado']['Location']['Lon'] = d['Lon']
     
        #outros dados
        for s in NomeDosDados:
            tupla.dat['Dado'][s] = d[s]

        Doc.Boia['Data'].append(deepcopy(tupla.dat))
        
   
 #   pprint.pprint(Doc.Boia)
    print(NomeBoia + " - Completo")
    logFile=open('log' + '-'+ NomeBoia + '.txt', 'w')
    pprint.pprint(Doc.Boia, logFile)
    #return True
    return AdicionarBoiaBanco(deepcopy(Doc.Boia))
    #enviar o dict para o banco

def AdicionarBoiaBanco(obj):
    client = MongoClient("mongodb+srv://Bessa:vEiz8yoTtgOZzhyC@brwindy-adtf0.mongodb.net/test?retryWrites=true&w=majority")    
    db=client.admin
    # Issue the serverStatus command and print the results
  #  serverStatusResult=db.command("serverStatus")
    #pprint(serverStatusResult)
    db=client.Brwindy
    if(db.PostsTest.find({'Nome':obj['Name']}).count() == 1 ):
        return False
    result=db.PostsTest.insert_one(obj)
    #pprint.pprint(result)
    return result



def AdicionarBoiasPasta(path):
#CsvToDict(pathArquivo="../DadosOriginais/Dados - Boias - Marinha - Qualificados - 2018-05-07/fortaleza.csv", NomeBoia="fortaleza")
   # path = "../DadosOriginais/Dados - Boias - Marinha - Qualificados - 2018-05-07"
    datadir = os.listdir(path)
    print(datadir)

    for boia in datadir:
        nome = boia.replace(".csv","")
        ret = CsvToDict(pathArquivo = path+'/'+boia, NomeBoia= nome)
        if(ret == False ):
            print("Error Na boia " + nome )

AdicionarBoiasPasta(path="../DadosOriginais/Dados - Boias - Marinha - Qualificados - 2018-05-07")

#CsvToDict(  pathArquivo="../DadosOriginais/Dados - Boias - Marinha - Qualificados - 2018-05-07/fortaleza.csv",  NomeBoia = 'fortaleza' )