def converter(currency_type, usd,):
    pesos = int(input('¿How many '+ currency_type + ' do you have? '))
    dollars = round(pesos / usd, 2)
    print('Do you have $' + str(dollars) + ' dollars')

menu = """
Welcome to the currency converter

1 - Colombian Pesos
2 - Argentine Pesos
3 - Mexican Pesos

Choose an option: """

opcion = input(menu)

if opcion == '1':
    converter('colombian pesos', 3834.55)

elif opcion == '2':
    converter('argentine pesos', 95.84)

elif opcion == '3':
    converter('mexican pesos', 19.87)

else:
    print('Enter a correct value')