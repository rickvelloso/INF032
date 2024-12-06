valor_compra = float(input("Digite o valor de compra: "))
if valor_compra < 20:
    lucro = 0.45
else:
    lucro = 0.30

valor_venda = valor_compra * (1 + lucro)
print(f"O valor de venda é: R$ {valor_venda:.2f}")
