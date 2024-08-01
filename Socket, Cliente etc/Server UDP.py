import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print('Socket criado com sucesso.')

host = 'localhost'
porta = 5433

#Usado para ligar o servidor e cliente
s.bind((host, porta))
mensagem = 'Servidor: Olá Cliente.'

while 1:
    dados, endereco = s.recvfrom(4096)

    if dados:
        print('Servidor enviando mensagem.')
        s.sendto(mensagem.encode(), endereco)
    
    print('Servidor encerrado.')
    break

