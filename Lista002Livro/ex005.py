import math

a = float(input("Digite o valor de A: "))
b = float(input("Digite o valor de B: "))
c = float(input("Digite o valor de C: "))

delta = b**2 - 4*a*c

if delta < 0:
    print("Não existem raízes reais.")
elif delta == 0:
    x = -b / (2 * a)
    print(f"Raiz única: x = {x:.2f}")
else:
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)
    print(f"Duas raízes: x1 = {x1:.2f}, x2 = {x2:.2f}")
