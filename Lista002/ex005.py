tempo = float(input("Digite o tempo gasto na viagem (em horas): "))
velocidade_media = float(input("Digite a velocidade média (em km/h): "))

distancia = velocidade_media * tempo
litros_gastos = distancia / 12

print("Velocidade Média: {} km/h".format(velocidade_media))
print("Tempo Gasto: {} horas".format(tempo))
print("Distância Percorrida: {} km".format(distancia))
print("Quantidade de Litros Gastos: {:.2f} litros".format(litros_gastos))
