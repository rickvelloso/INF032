quantidade_fitas = int(input("Digite a quantidade de fitas: "))
valor_aluguel = float(input("Digite o valor de aluguel por fita: "))

fitas_alugadas_mes = quantidade_fitas / 3
faturamento_anual = fitas_alugadas_mes * valor_aluguel * 12
fitas_atrasadas_mes = fitas_alugadas_mes / 10
ganho_multas_mes = fitas_atrasadas_mes * valor_aluguel * 0.1
fitas_estragadas_ano = quantidade_fitas * 0.02
fitas_reposicao = quantidade_fitas / 10
fitas_finais = quantidade_fitas - fitas_estragadas_ano + fitas_reposicao

print("Faturamento anual: {:.2f}".format(faturamento_anual))
print("Ganho com multas por mês: {:.2f}".format(ganho_multas_mes))
print("Quantidade de fitas ao final do ano: {:.0f}".format(fitas_finais))
