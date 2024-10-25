preco_cerveja = 2.20
qtd_cerveja = 75

preco_macarrao = 8.73
qtd_macarrao = 2

preco_molho = 3.45
qtd_molho = 1

preco_cebola_kg = 5.40
qtd_cebola_kg = 0.420

preco_alho_kg = 30.00
qtd_alho_kg = 0.250

preco_pao_kg = 25.00
qtd_pao_kg = 0.450

total_cerveja = preco_cerveja * qtd_cerveja
total_macarrao = preco_macarrao * qtd_macarrao
total_molho = preco_molho * qtd_molho
total_cebola = preco_cebola_kg * qtd_cebola_kg
total_alho = preco_alho_kg * qtd_alho_kg
total_pao = preco_pao_kg * qtd_pao_kg

total_compra = total_cerveja + total_macarrao + total_molho + total_cebola + total_alho + total_pao

integrantes = 5
valor_por_integrante = total_compra / integrantes

print(f"Total da compra: R$ {total_compra:.2f}")
print(f"Valor por integrante: R$ {valor_por_integrante:.2f}")


