'''Crie um programa que cadastre locais históricos do mundo com suas coordenadas, fazendo uso de tuplas com parâmetros nomeados. Dica: use a função namedtuple().'''
from collections import namedtuple

locais = []
Local = namedtuple('Local', ['nome','latitude','longitude'])
while True:
    nome = input('Nome do local: ')
    latitude = float(input('Latitude: '))
    longitude = float(input('Longitude: '))
    local = Local(nome=nome, latitude=latitude, longitude=longitude)
    locais.append(local)
    if input('Cadastrar mais locais? (s/n) ').lower() == 'n':
        break
for local in locais:
    print(f'Localidade: {local.nome}')
    print(f'Coordenadas: ({local.latitude}, {local.longitude})')