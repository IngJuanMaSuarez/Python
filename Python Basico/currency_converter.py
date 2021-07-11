menu = """
Bienvenido al conversor de monedas

1 - Pesos Colombianos
2 - Pesos Argentinos
3 - Pesos Mexicanos

Elige una opción: """

opcion = input(menu)

if opcion == '1':
    cop = int(input('¿How many colombian pesos do you have? '))
    usd = 3834.55
    dollars = cop / usd
    dollars = round(dollars, 2)
    print('Do you have $' + str(dollars) + ' dollars')

elif opcion == '2':
    cop = int(input('¿How many argentine pesos do you have? '))
    usd = 95.84
    dollars = cop / usd
    dollars = round(dollars, 2)
    print('Do you have $' + str(dollars) + ' dollars')

elif opcion == '3':
    cop = int(input('¿How many mexican pesos do you have? '))
    usd = 19.87
    dollars = cop / usd
    dollars = round(dollars, 2)
    print('Do you have $' + str(dollars) + ' dollars')

else:
    print('Enter a correct value')