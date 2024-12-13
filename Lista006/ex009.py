
def energy_consumption():
    total_residential = 0
    total_commercial = 0
    total_industrial = 0

    while True:
        consumer_number = int(input("Número do consumidor (0 para sair): "))
        if consumer_number == 0:
            break
        kwh = float(input("Quantidade de kWh consumidos: "))
        consumer_type = int(input("Tipo do consumidor (1-Residencial, 2-Comercial, 3-Industrial): "))

        if consumer_type == 1:
            cost = kwh * 0.3
            total_residential += kwh
        elif consumer_type == 2:
            cost = kwh * 0.5
            total_commercial += kwh
        elif consumer_type == 3:
            cost = kwh * 0.7
            total_industrial += kwh
        else:
            print("Tipo de consumidor inválido.")
            continue

        print(f"Custo total para o consumidor {consumer_number}: R$ {cost:.2f}")

    total_consumption = total_residential + total_commercial + total_industrial
    print(f"Consumo total residencial: {total_residential} kWh")
    print(f"Consumo total comercial: {total_commercial} kWh")
    print(f"Consumo total industrial: {total_industrial} kWh")
    print(f"Média de consumo (residencial e comercial): {(total_residential + total_commercial) / 2:.2f} kWh")
    
energy_consumption()
