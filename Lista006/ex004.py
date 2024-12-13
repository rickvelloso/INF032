
def count_numbers_between():
    count = 0
    while True:
        number = int(input("Digite um número (0 para sair): "))
        if number == 0:
            break
        if 100 <= number <= 200:
            count += 1
    print(f"Você digitou {count} números entre 100 e 200.")
    
count_numbers_between()
