import random, string

tamanho = int(input('Digite o tamanho desejado para a senha: '))
chars = string.ascii_letters + string.digits + '!"#$%&()*+,-./:;<=>?@[\]^_`{|}~'
rng = random.SystemRandom()

senha = ''.join(rng.choice(chars) for i in range(tamanho))
print(f'A senha gerada é {senha}')

