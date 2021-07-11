cop = int(input("¿How many colombian pesos do you have? "))
usd = 3834.55
dollars = cop / usd
dollars = round(dollars, 2)
print("Do you have $" + str(dollars) + " dollars")