
def triple_numbers():
    while True:
        number = int(input("Digite um número (999 para sair): "))
        if number == 999:
            break
        print(f"O triplo de {number} é {number * 3}")

triple_numbers()


