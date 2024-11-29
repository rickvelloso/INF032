compra = float(input("Digite o valor de compra: "))
venda = float(input("Digite o valor de venda: "))

lucro_percentual = ((venda - compra) / compra) * 100

if lucro_percentual < 10:
    print("Lucro menor que 10%.")
elif 10 <= lucro_percentual <= 20:
    print("Lucro entre 10% e 20%.")
else:
    print("Lucro superior a 20%.")
