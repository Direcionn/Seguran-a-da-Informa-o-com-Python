import os
import time

with open('hosts.txt', 'r') as file:
    #linha = file.read()
    linha = file.readlines()

for ip in linha:
    #ip = linha.strip()
    print(f'Verificando o ip {ip}')
    os.system(f'ping -n 4 {ip}')
    #Tempo de colddown entre uma leitura e outra.
    time.sleep(2)

