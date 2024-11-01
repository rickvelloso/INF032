emprestimo = float(input("Digite o valor do empréstimo: "))
taxa_juros = float(input("Digite a taxa de juros (%): "))
meses = int(input("Digite a quantidade de meses: "))

prestacao = emprestimo * (1 + (taxa_juros / 100) * meses)

print("Valor da Prestação: {:.2f}".format(prestacao))
