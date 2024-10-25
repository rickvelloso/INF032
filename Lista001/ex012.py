import math

x = 15
y = 10
z = 13

volume_pote = x * y * z

raio_bolinha = 1.2
volume_bolinha = (4/3) * math.pi * (raio_bolinha ** 3)

fator_empacotamento = 0.74

volume_util = volume_pote * fator_empacotamento

numero_bolinhas = volume_util // volume_bolinha

print(f"Cabem aproximadamente {int(numero_bolinhas)} bolinhas de queijo no pote de sorvete.")
