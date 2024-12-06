salario = float(input("Digite o salário bruto: "))
prestacao = float(input("Digite o valor da prestação: "))

if prestacao <= 0.3 * salario:
    print("O empréstimo pode ser concedido.")
else:
    print("O empréstimo não pode ser concedido.")
