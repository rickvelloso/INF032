valor_compra = float(input("Digite o valor da compra: "))

if valor_compra <= 20:
    desconto = 5
elif valor_compra <= 50:
    desconto = 10
elif valor_compra <= 100:
    desconto = 15
elif valor_compra <= 1000:
    desconto = 20
else:
    desconto = 30

valor_final = valor_compra - (valor_compra * desconto / 100)
print(f"Desconto: {desconto}%, Valor a ser pago: R${valor_final:.2f}")
