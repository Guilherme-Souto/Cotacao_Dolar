import requests
import json

lista_euro = []
lista_dolar = []

search = requests.get(
    'https://economia.awesomeapi.com.br/json/daily/USD-BRL/7')
search = search.json()

search_eu = requests.get(
    'https://economia.awesomeapi.com.br/json/daily/EUR-BRL/7')
search_euro = search_eu.json()

x = 0
for dicio in search:
    dicio = search[x]["bid"]
    lista_dolar.append(dicio)
    x += 1

y = 0
for dicio in search_euro:
    dicio = search_euro[y]["bid"]
    lista_euro.append(dicio)
    y += 1


print("variação do dolar na ultima semana: ", lista_dolar)
print("variação do Euro na ultima semana: ", lista_euro)
