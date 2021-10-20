menu = """
Bienvenido al conversor de monedas

1 - Pesos colombianos
2 - Pesos argentinos
3 - Pesos mexicanos

Elige una opcion: 
"""
opcion = int(input(menu))

if opcion == 1:
    peso_colombiano = int(input("Cuantos pesos colombianos tienes?: "))
    valor_dolar = 3875
    dolares = peso_colombiano / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dolares")
elif opcion == 2:
    peso_argentino = int(input("Cuantos pesos argentinos tienes?: "))
    valor_dolar = 180
    dolares = peso_argentino / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dolares")
elif opcion == 3:
    peso_mexicano = int(input("Cuantos pesos mexicanos tienes?: "))
    valor_dolar = 24
    dolares = peso_mexicano / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dolares")
else:
    print ("Ingrese una opcion correcta por favor")



