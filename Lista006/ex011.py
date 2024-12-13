
def calculate_excess_weight():
    weight = float(input("Digite o peso dos peixes (kg): "))
    excess = max(0, weight - 50)  # Excesso acima de 50 kg
    fine = excess * 4  # Multa de R$ 4,00 por quilo excedente
    print(f"Peso total: {weight} kg")
    print(f"Excesso: {excess} kg")
    print(f"Multa: R$ {fine:.2f}")
    
calculate_excess_weight()
