"""**append()**Este método agrega un elemento al final de una lista.

**count()**Este método recibe un elemento como argumento, y cuenta la cantidad de veces que aparece en la lista.

**extend()**Este método extiende una lista agregando un iterable al final.

**index()**Este método recibe un elemento como argumento, y devuelve el índice de su primera aparición en la lista.

**insert()**Este método inserta el elemento x en la lista, en el índice i.

**pop()**Este método devuelve el último elemento de la lista, y lo borra de la misma.

**remove()**Este método recibe como argumento un elemento, y borra su primera aparición en la lista.

**reverse()**Este método invierte el orden de los elementos de una lista.

**sort()**Este método ordena los elementos de una lista.

**Convertir a listas**Para convertir a tipos listas debe usar la función list() la cual esta integrada en el interprete Python."""

"""append()
Añade un ítem al final de la lista:

lista = [1,2,3,4,5]
lista.append(6)
print(lista)
# [1, 2, 3, 4, 5, 6]
clear()
Vacía todos los ítems de una lista:

lista = [1,2,3,4,5]
lista.clear()
#[]
extend()
Une una lista a otra:

l1 = [1,2,3]
l2 = [4,5,6]
l1.extend(l2)
#[1, 2, 3, 4, 5, 6]
count()
Cuenta el número de veces que aparece un ítem:

["Hola", "mundo", "mundo"].count("Hola")
#1
index()
Devuelve el índice en el que aparece un ítem (error si no aparece):

["Hola", "mundo", "mundo"].count("Hola")
#0
insert()
Agrega un ítem a la lista en un índice específico:

l = [1,2,3]
l.insert(0,0) #(index , element) first position 0, second last position -1
							#last position len
# [ 0, 1 , 2 , 3 ]
pop()
Extrae un ítem de la lista y lo borra:

l = [10,20,30,40,50]
print(l.pop())
print(l)

#50
#[10, 20, 30, 40]
Podemos indicarle un índice con el elemento a sacar (0 es el primer ítem):

print(l.pop(0))
print(l)

#10
#[20, 30, 40]
remove()
Borra el primer ítem de la lista cuyo valor concuerde con el que indicamos:

l = [20,30,30,30,40]
l.remove(30)
print(l)
#[20, 30, 30, 40]
reverse()
Le da la vuelta a la lista actual:

l.reverse()
print(l)
#[40, 30, 30, 20]
Las cadenas no tienen el método .reverse() pero podemos simularlo haciendo unas conversiones:

lista = list("Hola mundo")
lista.reverse()
cadena = "".join(lista)
cadena
#'odnum aloH'
sort()
Ordena automáticamente los ítems de una lista por su valor de menor a mayor:

lista = [5,-10,35,0,-65,100]
lista.sort()
lista
#[-65, -10, 0, 5, 35, 100]
Podemos utilizar el argumento reverse=True para indicar que la ordene del revés:

lista.sort(reverse=True)
lista
#[100, 35, 5, 0, -10, -65]
"""