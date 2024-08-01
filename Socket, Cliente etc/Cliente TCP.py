import socket
import sys

def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as e:
        print('A conexão falhou.')
        print(f'Erro: {e}')
        sys.exit()
    print('Socket criado com sucesso.')

    Host = input("Digite o host ou ip desejado: ")
    Porta = input('Digite a porta a ser conectada: ')
    
    try:
        s.connect((Host, int(Porta)))
        print(f'Cliente TCP conectado com sucesso no Host: {Host} e na Porta: {Porta}.')
        #O shutdown é usado para fechar a conexão depois de um tempo pré-determinado, para não gerar loop infinito.
        s.shutdown(2)
    except socket.error as e:
        print(f'A conexão com o Host: {Host} e Porta: {Porta} FALHOU.')
        print(f'Erro: {e}.')
        sys.exit()

main()

