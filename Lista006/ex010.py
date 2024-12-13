
import math

def paint_store():
    area = float(input("Tamanho da área a ser pintada em metros quadrados: "))
    liters_needed = math.ceil(area / 6 * 1.1)  # Inclui 10% de folga

    cans_18l = math.ceil(liters_needed / 18)
    cost_18l = cans_18l * 80

    gallons_3_6l = math.ceil(liters_needed / 3.6)
    cost_3_6l = gallons_3_6l * 25

    mixed_cans = liters_needed // 18
    mixed_gallons = math.ceil((liters_needed % 18) / 3.6)
    cost_mixed = mixed_cans * 80 + mixed_gallons * 25

    print(f"Apenas latas de 18L: {cans_18l} latas, custo: R$ {cost_18l:.2f}")
    print(f"Apenas galões de 3,6L: {gallons_3_6l} galões, custo: R$ {cost_3_6l:.2f}")
    print(f"Mistura: {mixed_cans} latas e {mixed_gallons} galões, custo: R$ {cost_mixed:.2f}")
    

paint_store()
