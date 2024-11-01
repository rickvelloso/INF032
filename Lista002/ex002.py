num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))
num4 = float(input("Digite o quarto número: "))

media_ponderada = (num1*1 + num2*2 + num3*3 + num4*4) / (1 + 2 + 3 + 4)

print("Média Ponderada: {:.2f}".format(media_ponderada))
