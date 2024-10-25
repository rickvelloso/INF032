### Fazendo com Estrutura de dados: ###

compras = [
    {"item": "Cerveja", "preco": 2.20, "quantidade": 75},
    {"item": "Macarrão", "preco": 8.73, "quantidade": 2},
    {"item": "Molho de tomate", "preco": 3.45, "quantidade": 1},
    {"item": "Cebola", "preco": 5.40, "quantidade": 0.420},  
    {"item": "Alho", "preco": 30.00, "quantidade": 0.250},  
    {"item": "Pães franceses", "preco": 25.00, "quantidade": 0.450}  
]

total_compra = 0
for compra in compras:
    total_item = compra["preco"] * compra["quantidade"]
    total_compra += total_item
    print(f"{compra['item']}: R$ {total_item:.2f}")

integrantes = 5
valor_por_integrante = total_compra / integrantes

print(f"\nTotal da compra: R$ {total_compra:.2f}")
print(f"Valor por integrante: R$ {valor_por_integrante:.2f}")
