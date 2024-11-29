n = int(input("Digite o total de vendas: "))
soma_pares = 0
soma_impares = 0

for _ in range(n):
    num = int(input("Digite o número da venda: "))
    if num % 2 == 0:
        soma_pares += num
    else:
        soma_impares += num

print(f"Soma dos pares: {soma_pares}, Soma dos ímpares: {soma_impares}")
