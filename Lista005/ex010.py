municipio = input("Digite o nome do município: ")
eleitores = int(input("Digite a quantidade de eleitores aptos: "))
votos = int(input("Digite a quantidade de votos do candidato mais votado: "))

if eleitores > 20000 and votos <= (0.5 * eleitores):
    print(f"O município {municipio} terá segundo turno.")
else:
    print(f"O município {municipio} não terá segundo turno.")
