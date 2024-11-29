baixa = float(input("Digite a baixa histórica: "))
alta = float(input("Digite a alta histórica: "))
atual = float(input("Digite o preço atual: "))

intervalo = alta - baixa
suporte = baixa + (intervalo * 0.3)
resistencia = baixa + (intervalo * 0.6)

print(f"Suporte: {suporte:.2f}, Resistência: {resistencia:.2f}")
if suporte <= atual <= resistencia:
    print("O preço está dentro da faixa de suporte-resistência.")
else:
    print("O preço está fora da faixa de suporte-resistência.")
