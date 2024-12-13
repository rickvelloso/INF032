
def print_first_character():
    while True:
        name = input("Digite um nome (FIM para sair): ")
        if name.upper() == "FIM":
            break
        print(f"O primeiro caractere de {name} é {name[0]}")
        
print_first_character()


