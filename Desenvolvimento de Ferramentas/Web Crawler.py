import requests
from bs4 import BeautifulSoup
from collections import Counter
import string

# Esta função é responsável por buscar o conteúdo da URL fornecida, processar o HTML e extrair palavras.
def start(url):
    wordlist = []
    source_code = requests.get(url).text

    soup = BeautifulSoup(source_code, 'html.parser')

    # Tente várias opções de seletores comuns
    possible_selectors = [
        'div', 'article', 'main',  # Seletor genérico
        {'class': 'content'},  # Exemplo de classe
        {'class': 'main-content'},  # Exemplo de classe
        {'class': 'post-content'},  # Exemplo de classe
    ]

    found_divs = []
    for selector in possible_selectors:
        if isinstance(selector, str):
            divs = soup.findAll(selector)
        else:
            divs = soup.findAll('div', selector)
        
        if divs:
            found_divs.extend(divs)
            print(f"Found {len(divs)} elements with selector {selector}")

    if not found_divs:
        print("No matching elements found.")
        return

    for cada_texto in found_divs:
        content = cada_texto.text

        words = content.lower().split()
        print("Words Preview:", words[:10])  # Imprime as primeiras 10 palavras

        for cada_palavra in words:
            wordlist.append(cada_palavra)

    limpar_wordlist(wordlist)

# Esta função remove caracteres indesejados e limpa a lista de palavras.
def limpar_wordlist(wordlist):
    limpar_lista = []
    simbolos = string.punctuation

    for palavra in wordlist:
        palavra = palavra.strip(simbolos)
        if len(palavra) > 0:
            limpar_lista.append(palavra)
    
    criar_dicionario(limpar_lista)
    
# Esta função conta a frequência das palavras e exibe as 10 palavras mais comuns.
def criar_dicionario(limpar_lista):
    contador_palavra = Counter(limpar_lista)

    for chave, valor in sorted(contador_palavra.items()):
        print('{} : {}'.format(chave, valor))

    top = contador_palavra.most_common(10)
    print(top)

if __name__ == '__main__':
    start("https://www.geeksforgeeks.org/python-programming-language-tutorial/")


