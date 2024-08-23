import phonenumbers
# Geocoder é usado para obter a localização geográfica associada a um número de telefone.
from phonenumbers import geocoder

telefone = input('Digite o telefone no formato: +5511*********: ')

# O input do usuario será transformado em um formato de telefone na variavel abaixo.
numero_telefone = phonenumbers.parse(telefone)

print(geocoder.description_for_number(numero_telefone, 'pt'))


