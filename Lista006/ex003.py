
def average_positive_numbers():
    total = 0
    count = 0
    while True:
        number = int(input("Digite um número positivo (0 para sair): "))
        if number == 0:
            break
        total += number
        count += 1
    if count > 0:
        print(f"A média dos números digitados é {total / count}")
    else:
        print("Nenhum número foi digitado.")
        
average_positive_numbers()
