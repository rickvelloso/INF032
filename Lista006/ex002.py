
def count_positive_numbers():
    count = 0
    while True:
        number = int(input("Digite um número positivo (negativo para sair): "))
        if number < 0:
            break
        count += 1
    print(f"Você digitou {count} números positivos.")
    
count_positive_numbers()
