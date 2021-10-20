dolar = int(input("Cuantos dolares tienes?: "))
valor_pesos_argentinos = 180
pesos_argentinos = dolar * valor_pesos_argentinos
pesos_argentinos = round(pesos_argentinos, 2)
pesos_argentinos = str(pesos_argentinos)
print("Tienes $" + pesos_argentinos + " pesos argentinos")