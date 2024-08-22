import hashlib
import sys
"""
resultado = hashlib.md5(b'Python Security')

print(f'O hash da string é {resultado.hexdigest()}')
"""

"""
texto = input("Digite o texto para ser gerado a hash: ")

resultado = hashlib.md5(texto.encode('utf-8'))

print(f'A hash md5 do texto inserido é: {resultado.hexdigest()}')
"""

while  True:
    menu = int(input('''
    Menu - Escolha o tipo de Hash desejada:
    1) MD5
    2) SHA1
    3) SHA256
    4) SHA512
    0) Sair do programa
    Digite o número so Hash: '''))
    if menu < 0 or menu >= 4:
        print('Por questões de segurança o programa foi fechado.')
        break
    elif menu == 0:
        print('Obrigado pela preferência.')
        break
    
    texto = input("Digite o texto para ser gerado a hash: ")

    #A função encode em Python é utilizada para converter uma string (texto) em uma sequência de bytes
    if menu == 1:
        resultado = hashlib.md5(texto.encode('utf-8'))
        print(f'A hash MD5 do texto inserido é: {resultado.hexdigest()}')
    elif menu == 2:
        resultado = hashlib.sha1(texto.encode('utf-8'))
        print(f'A hash SHA1 do texto inserido é: {resultado.hexdigest()}')
    elif menu == 3:
        resultado = hashlib.sha256(texto.encode('utf-8'))
        print(f'A hash SHA256 do texto inserido é: {resultado.hexdigest()}')
    elif menu == 4:
        resultado = hashlib.sha512(texto.encode('utf-8'))
        print(f'A hash SHA512 do texto inserido é: {resultado.hexdigest()}')


