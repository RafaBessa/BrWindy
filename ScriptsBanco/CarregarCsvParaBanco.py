import csv
from pymongo import MongoClient
from pprint import pprint
import os
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
    Dado = {}
    NomeDosDados = ['# Epoca','Wspd','Wspdflag','Wdir','Gust','Atmp', 
                    'Pres','Dewp','Humi','Arad','Wtmp','Wvht','Wmax','Dpd','Mwd','Spred']
    #transformar o csv em dict
    for d in dados:            
        #Pegar a Data
        if(d['Year'] != '2016' ):
            continue
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
        #print(Dado)
       # print('-----------------------------------------------------')
        # i+=1
        # if(i>3):
        #     break
    #print(Boia)
    Boia['Name'] = NomeBoia
    print(NomeBoia + " - Completo")
    return AdicionarBoiaBanco(Boia)
    #enviar o dict para o banco

def AdicionarBoiaBanco(obj):
    client = MongoClient("mongodb+srv://Bessa:vEiz8yoTtgOZzhyC@brwindy-adtf0.mongodb.net/test?retryWrites=true&w=majority")    
    db=client.admin
    # Issue the serverStatus command and print the results
  #  serverStatusResult=db.command("serverStatus")
    #pprint(serverStatusResult)
    db=client.Brwindy
    if(db.Posts2.find({'Nome':obj['Name']}).count() == 1 ):
        return False
    result=db.Posts2.insert_one(obj)
    pprint(result)




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