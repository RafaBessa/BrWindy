

# Pegar os dados do banco
# Fazer uma media do Wspd por mes
# Aplicar metodos de clustering

import requests
import json
import ast
class boia:
    Name = ''
    dados = {'1':0.0,
            '2':0.0,
            '3':0.0,
            '4':0.0,
            '5':0.0,
            '6':0.0,
            '7':0.0,
            '8':0.0,
            '9':0.0,
            '10':0.0,
            '11':0.0,
            '12':0.0,}

nomes = requests.get('http://127.0.0.1:5002/boiasNomes').json()
print(nomes)

#for n in nomes: 

#print(requests.get('http://127.0.0.1:5002/boia/santos').json())

boiaJson = requests.get('http://127.0.0.1:5002/boia/santos').json()
boiaJson = json.loads(boiaJson)[0]
#print(boiaJson)
#boiaJson = ast.literal_eval(boiaJson)
#boiaJson = boiaJson[0]
boiaMedia = boia()
boiaMedia.Name = boiaJson['Name']
qqt = [0]*13
for d in boiaJson['Data']:
    if(float((d['Wspd']).replace(',','.')) < -9000):
        continue
    qqt[int(d['Date']['Month'])] += 1
    boiaMedia.dados[str(d['Date']['Month'])] += float((d['Wspd']).replace(',','.'))

for i in range(1,13):
    print(boiaMedia.dados[str(i)])
    print(qqt[i])
    print(i)
    print("--")
    #boiaMedia.dados[str(i)] = boiaMedia.dados[str(i)]/qqt[i]
print(boiaMedia.dados)