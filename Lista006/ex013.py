
def calculate_meat_price():
    print("Tipos de carne: 1-File Duplo, 2-Alcatra, 3-Picanha")
    meat_type = int(input("Escolha o tipo de carne: "))
    weight = float(input("Quantidade de carne (kg): "))
    tabajara_card = input("Pagamento com cartão Tabajara? (S/N): ").upper()

    if meat_type == 1:
        price_per_kg = 4.9 if weight <= 5 else 5.8
        meat_name = "File Duplo"
    elif meat_type == 2:
        price_per_kg = 5.9 if weight <= 5 else 6.8
        meat_name = "Alcatra"
    elif meat_type == 3:
        price_per_kg = 6.9 if weight <= 5 else 7.8
        meat_name = "Picanha"
    else:
        print("Tipo de carne inválido.")
        return

    total_price = weight * price_per_kg
    discount = total_price * 0.05 if tabajara_card == "S" else 0
    final_price = total_price - discount

    print(f"Tipo de carne: {meat_name}")
    print(f"Quantidade: {weight:.2f} kg")
    print(f"Preço total: R$ {total_price:.2f}")
    print(f"Desconto: R$ {discount:.2f}")
    print(f"Valor a pagar: R$ {final_price:.2f}")
    
calculate_meat_price()
