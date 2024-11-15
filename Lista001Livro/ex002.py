import math

# Assumindo as constantes
x = 3
y = 6

# (a) w = e^x - ln(y)
w = math.exp(x) - math.log(y)
print("w =", w)

# (b) z = x * y^2 + y * cos(x)
z = x * (y**2) + y * math.cos(x)
print("z =", z)

# (c) s = x/y + (x + y) + ln(x) + tan(y)
s = (x / y) + (x + y) + math.log(x) + math.tan(y)
print("s =", s)
