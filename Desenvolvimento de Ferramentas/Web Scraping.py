# BeautifulSoup - Usada para extração de dados de arquivos HTML e XML.
from bs4 import BeautifulSoup
# Requests - Permite solicitações HTTP em Python.
import requests

site = requests.get('https://www.youtube.com').content

soup = BeautifulSoup(site, 'html.parser')

print(soup.prettify())


