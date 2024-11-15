# Lista de números
num = [3, 3, 4, 1, 2, 1, 1, 2, 3, 4, 4, 1, 1, 5, 2]

# (a) Fatiar do elemento de índice 2 ao de índice 3
print("a) Elementos de índice 2 ao 3:", num[2:4])

# (b) Fatiar do quinto elemento ao nono elemento
print("b) Quinto ao nono elemento:", num[4:9])

# (c) Fatiar do elemento de índice 1 ao último
print("c) Índice 1 ao último:", num[1:])

# (d) Fatiar do primeiro elemento ao último
print("d) Primeiro ao último:", num[:])

# (e) Fatiar do primeiro elemento ao último saltando de três em três elementos
print("e) Primeiro ao último saltando de 3:", num[::3])

# (f) Selecionar o último elemento da lista
print("f) Último elemento:", num[-1])

# (g) Selecionar os três últimos elementos da lista
print("g) Três últimos elementos:", num[-3:])

# (h) Selecionar os quatro primeiros elementos da lista
print("h) Quatro primeiros elementos:", num[:4])

# (i) Contar o número de elementos da lista
print("i) Número de elementos da lista:", len(num))

# (j) Contar quantas vezes aparece o número 1 na lista
print("j) Número 1 aparece:", num.count(1), "vezes")
