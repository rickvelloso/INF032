num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

numeros = sorted([num1, num2, num3])
menor, intermediario, maior = numeros

print(f"Menor: {menor}, Intermediário: {intermediario}, Maior: {maior}")
