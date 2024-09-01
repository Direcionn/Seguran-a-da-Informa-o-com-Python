import re
import json
from urllib.request import urlopen

# url: https://ipinfo.io/json
url = input('Digite a url para saber o ip da maquina, na url é necessario colocar https:// antes do site: ')
resposta = urlopen(url)

dados = json.load(resposta)
ip = dados['ip']
nome_host = dados['hostname']
cidade = dados['city']
estado = dados['region']
pais = dados['country']
coordenadas = dados['loc']
organizacao = dados['org']
cep = dados['postal']
fuso_horario = dados['timezone']
site = dados['readme']

print(f"""Dados da url informada:
IP: {ip}
hostname: {nome_host}
city: {cidade}
region: {estado}
country: {pais}
loc: {coordenadas}
org: {organizacao}
postal: {cep}
timezone: {fuso_horario}
readme: {site}
""")


