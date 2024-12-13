
def population_growth():
    population_a = 5000000
    population_b = 7000000
    growth_rate_a = 0.03
    growth_rate_b = 0.02
    years = 0

    while population_a <= population_b:
        population_a += population_a * growth_rate_a
        population_b += population_b * growth_rate_b
        years += 1

    print(f"Serão necessários {years} anos para a população do país A ultrapassar a do país B.")
    
population_growth()

