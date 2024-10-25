import math

base = 10
altura = 5

perimetro = 2 * (base + altura)
area = base * altura
diagonal = math.sqrt(base ** 2 + altura ** 2)

print(f"Perímetro: {perimetro} cm")
print(f"Área: {area} cm²")
print(f"Diagonal: {diagonal:.2f} cm")
