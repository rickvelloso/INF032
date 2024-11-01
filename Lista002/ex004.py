valor_hora = float(input("Digite o valor da hora-aula: "))
numero_aulas = int(input("Digite o número de aulas dadas: "))
percentual_desconto = float(input("Digite o percentual de desconto do INSS: "))

salario_bruto = valor_hora * numero_aulas
desconto = salario_bruto * (percentual_desconto / 100)
salario_liquido = salario_bruto - desconto

print("Salário Líquido: {:.2f}".format(salario_liquido))
