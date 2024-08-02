#Usado para ter os dois carros correndo ao mesmo tempo.
import threading
#Usado para determinar um tempo de coldown entre uma incrementação e outra.
import time
#Usado para ter uma velocidade aleatoria.
import random

class Corrida:
    def __init__(self):
        self.piloto1_pos = 0
        self.piloto2_pos = 0
        self.velocidade1 = random.randint(1, 10)
        self.velocidade2 = random.randint(1, 10)
        self.vencedor = None
        self.lock = threading.Lock()
        self.finish_event = threading.Event()

    def carro(self, piloto, piloto_num):
        trajeto = 0
        while trajeto <= 100 and not self.finish_event.is_set():
            with self.lock:
                if piloto_num == 1:
                    velocidade = self.velocidade1
                else:
                    velocidade = self.velocidade2
            trajeto += velocidade
            #Coldown entre uma incrementação e outra
            time.sleep(0.5)
            print(f'Piloto: {piloto} KM: {trajeto}.\n')
            with self.lock:
                if piloto_num == 1:
                    self.piloto1_pos = trajeto
                elif piloto_num == 2:
                    self.piloto2_pos = trajeto
                if trajeto >= 100 and self.vencedor is None:
                    self.vencedor = piloto
                    self.finish_event.set()

    def set_velocidade(self, piloto_num, nova_velocidade):
        with self.lock:
            if piloto_num == 1:
                self.velocidade1 = nova_velocidade
                print(f'Velocidade do {piloto1} alterada para: {nova_velocidade}')
            elif piloto_num == 2:
                self.velocidade2 = nova_velocidade
                print(f'Velocidade do {piloto2} alterada para: {nova_velocidade}')

piloto1 = input('Digite o nome do piloto: ')
piloto2 = input('Digite o nome do piloto: ')

#Instancia a classe Corrida.
corrida = Corrida()

#Inseri os argumentos necessários para a classe 'carro' funcionar.
t_carro1 = threading.Thread(target = corrida.carro, args = [piloto1, 1])
t_carro2 = threading.Thread(target = corrida.carro, args = [piloto2, 2])

#Inicia as threads(carro).
t_carro1.start()
t_carro2.start()

#Cria uma velocidade para cada piloto de modo randomico.
while not corrida.finish_event.is_set():
    time.sleep(1.7)
    corrida.set_velocidade(1, random.randint(1, 10))
    corrida.set_velocidade(2, random.randint(1, 10))

#Espera as threads(carro) terminarem.
t_carro1.join()
t_carro2.join()

#Exibir posteriormente a colocação de cada piloto.
if corrida.vencedor == piloto1:
    segundo = piloto2
else:
    segundo = piloto1

print(f'O piloto {corrida.vencedor} ganhou a corrida.')
print(f'O piloto {segundo} terminou em segundo.')

