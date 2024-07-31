#Importa a biblioteca 'Operation System'
import os

ip_ou_host = input('Digite o ip ou host a ser verificado: ')

#Utiliza a biblioteca para informar o ping do ip ou host informado
os.system('ping -n 6 {}'.format(ip_ou_host))


