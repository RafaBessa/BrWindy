import csv
from pymongo import MongoClient
from pprint import pprint
def CsvToDict(pathArquivo,NomeBoia):
   

    arquivo = open(pathArquivo)

    dados = csv.DictReader(arquivo)

    #i=0
    Boia = {'Name':"",
            'Data':[ ],
    }


    Date = {'Year':'', 'Month':'','Day':'', 'Hour':'','Minute':''}
    Location = {'Lat':'', 'Lon':''}

    Dado = { '# Epoca':'',
            'Date':{}, 
            'Location':{},
            'Battery':'',
            'bHead':'',
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
            'Cvel1':'',
            'Cdir1':'',
            'Cvel2':'',
            'Cdir2':'',
            'Cvel3':'',
            'Cdir3':'',
            'Wvht':'',
            'Wmax':'',
            'Dpd':'',
            'Mwd':'',
            'Spred':''
            }
    Dado = {}
    NomeDosDados = ['# Epoca','Battery','bHead','Wspd','Wspdflag','Wdir','Gust','Atmp', 
                    'Pres','Dewp','Humi','Arad','Wtmp','Cvel1','Cdir1','Cvel2',
                    'Cdir2','Cvel3','Cdir3','Wvht','Wmax','Dpd','Mwd','Spred']
    #transformar o csv em dict
    for d in dados:            
        #Pegar a Data
        Date['Year'] = d['Year']
        Date['Month'] = d['Month']
        Date['Day'] = d['Day']
        Date['Hour'] = d['Hour']
        Date['Minute'] = d['Minute']
        Dado['Date'] = Date
        #Pegar localizacao Lat':'', 'Lon'
        Location['Lat'] = d['Lat']
        Location['Lon'] = d['Lon']
        Dado['Location'] = Location
        #outros dados
        for s in NomeDosDados:
            Dado[s] = d[s]

        Boia['Data'].append(Dado)
        print(Dado)
        print('-----------------------------------------------------')
        # i+=1
        # if(i>3):
        #     break
    print(Boia)
    Boia['Nome'] = NomeBoia
    connectarbanco(Boia)
    #enviar o dict para o banco

def connectarbanco(obj):
    client = MongoClient("mongodb+srv://Bessa:vEiz8yoTtgOZzhyC@brwindy-adtf0.mongodb.net/test?retryWrites=true&w=majority")    
    db=client.admin
    # Issue the serverStatus command and print the results
    serverStatusResult=db.command("serverStatus")
    pprint(serverStatusResult)
    db=client.Brwindy
    result=db.Posts2.insert_one(obj)
    pprint(result)


CsvToDict(pathArquivo="../DadosOriginais/Dados - Boias - Marinha - Qualificados - 2018-05-07/fortaleza.csv", NomeBoia="fortaleza")
