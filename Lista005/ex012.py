num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
soma = num1 + num2

if soma > 20:
    soma += 8
else:
    soma -= 5

print(f"O resultado é: {soma}")
