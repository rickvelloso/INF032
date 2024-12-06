estado = input("Digite a sigla do estado: ").upper()
estados = {
    "RJ": "Carioca",
    "SP": "Paulista",
    "MG": "Mineira"
}

print(estados.get(estado, "Outros estados"))
