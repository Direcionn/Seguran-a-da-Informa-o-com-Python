import itertools

# A permutação é uma técnica de contagem utilizada para determinar quantas maneiras existem para ordenar os elementos de um conjunto finito.
# O número indica a quantiadade de letras que cada palavra pode possuir, as letras tem que estar de acordo com o número informado e a biblioteca não repete letra em cada palavra.
texto = input('Digite os carateres a serem permutados: ')
resultado = itertools.permutations(texto, len(texto))

for i in resultado:
    print("".join(i))
"""
resultado do for para tetxo 'abc':
abc
acb
bac
bca
cab
cba
"""

