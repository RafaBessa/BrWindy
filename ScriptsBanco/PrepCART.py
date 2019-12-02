import requests
import json
import ast
from pprint import pprint

boiaJson =  requests.get('http://127.0.0.1:5002/boia/portoseguro').json()
x = json.loads(boiaJson)[0]
#pprint(x['Data'][0])
dados = x['Data']
#pprint(dados)
relInfo = [
        'Month',
        'Wspd',
        'Wdir',
        'Atmp',
        'Pres',
        'Dewp',
        'Humi',
        'Wtmp',
        'Wvht',
        'Dpd',
        'Mwd']
#tirar os erros
for i in range(1,len(dados)):
    dados[i]['Dado']['Month'] = dados[i]['Dado']['Date']['Month']
    for info in relInfo:
        if(dados[i]['Dado'][info] == '-9999'):
            anterior = dados[i-1]['Dado'][info]
            j = i
            while(j<len(dados) and dados[j]['Dado'][info] == '-9999'):
                j+=1
                continue
            try:	    
                posterior = dados[j]['Dado'][info]
            except:
                posterior = anterior    
            dados[i]['Dado'][info] = round((float(anterior) + float(posterior))/2,2)

pprint(dados[9]) 

dados= dados[1:]
#save in a txt 
f= open("Prepportosegurosemgust.txt","w+")
#print the heads
head=""
for n in relInfo:
    head += n + ','
head = head[:len(head)-1]
head += '\n'

f.write(head)

for d in dados:
    pprint(d)
    line = ""
    for info in relInfo:
        line+= str(d['Dado'][info]).replace(",",".")+','
    line = line[:len(line)-1]
    line+='\n'
    f.write(line)

f.close()
