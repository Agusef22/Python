peso_argentino = int(input("Cuantos pesos argentinos tienes?: "))
valor_dolar = 180
dolares = peso_argentino / valor_dolar
dolares = round(dolares, 2)
dolares = str(dolares)
print("Tienes $" + dolares + " dolares")
