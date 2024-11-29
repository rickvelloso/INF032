n = int(input("Digite o número de termos (n): "))
soma = 0

for i in range(70, 70 - n, -1):
    soma += (70 - i) * i

print(f"Soma da série até o termo {n}: {soma}")
