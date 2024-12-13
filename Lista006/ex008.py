
def growth_comparison():
    height_chico = 1.5
    height_juca = 1.1
    growth_chico = 0.02
    growth_juca = 0.03
    years = 0

    while height_juca <= height_chico:
        height_chico += growth_chico
        height_juca += growth_juca
        years += 1

    print(f"Serão necessários {years} anos para Juca ser maior que Chico.")
    
growth_comparison()
