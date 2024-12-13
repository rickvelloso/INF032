
def print_divisors():
    while True:
        number = int(input("Digite um número (999 para sair): "))
        if number == 999:
            break
        print(f"Divisores de {number}: {[i for i in range(1, number + 1) if number % i == 0]}")
        
print_divisors()
