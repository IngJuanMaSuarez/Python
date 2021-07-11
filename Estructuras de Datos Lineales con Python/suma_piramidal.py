def suma_piramidal(limite_inferior, limite_superior, margen = 0):
    espacios_blanco = " " * margen
    print(espacios_blanco, limite_inferior, limite_superior)
    if limite_inferior > limite_superior:
        print(espacios_blanco, 0)
        return 0
    else:
        resultado = limite_inferior + suma_piramidal(limite_inferior + 1, limite_superior, margen + 4)
        print(espacios_blanco, resultado)
        return resultado

suma_piramidal(1, 4)