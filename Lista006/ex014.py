
def calculate_fuel_price():
    fuel_type = input("Tipo de combustível (A-álcool, G-gasolina): ").upper()
    liters = float(input("Quantidade de litros: "))

    if fuel_type == "A":
        price_per_liter = 1.9
        discount = 0.03 if liters <= 20 else 0.05
    elif fuel_type == "G":
        price_per_liter = 2.5
        discount = 0.04 if liters <= 20 else 0.06
    else:
        print("Tipo de combustível inválido.")
        return

    total_price = liters * price_per_liter
    discount_value = total_price * discount
    final_price = total_price - discount_value

    print(f"Tipo de combustível: {fuel_type}")
    print(f"Quantidade de litros: {liters:.2f}")
    print(f"Preço total: R$ {total_price:.2f}")
    print(f"Desconto: R$ {discount_value:.2f}")
    print(f"Valor a pagar: R$ {final_price:.2f}")
    
calculate_fuel_price()
