import hashlib

arquivo1 = r'Desenvolvimento de Ferramentas\arquivo1.txt'
arquivo2 = r'Desenvolvimento de Ferramentas\arquivo2.txt'

# Calcular o hash do primeiro arquivo
hash1 = hashlib.new('ripemd160')
with open(arquivo1, 'rb') as f1:
    hash1.update(f1.read())

# Calcular o hash do segundo arquivo
hash2 = hashlib.new('ripemd160')
with open(arquivo2, 'rb') as f2:
    hash2.update(f2.read())

# Obter os valores dos hashs
hash1_digest = hash1.hexdigest()
hash2_digest = hash2.hexdigest()

# Comparar os valores dos hashs
if hash1_digest == hash2_digest:
    print('Os hashs dos dois arquivos são iguais.')
else:
    print('Os hashs são DIFERENTES entre os dois arquivos comparados.')

# Imprimir os valores dos hashs
print(f'Hash do arquivo 1: {hash1_digest}')
print(f'Hash do arquivo 2: {hash2_digest}')

