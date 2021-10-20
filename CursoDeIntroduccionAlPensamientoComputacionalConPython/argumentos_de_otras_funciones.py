def multiplicar_por_dos(n):
    return n * 2

def sumar_dos(n):
    return n + 2

def operacion(f, numeros):
    resultados = []
    for numero in numeros:
        resultado = f(numero)
        resultados.append(resultado)
    return resultados

nums = [1, 2, 3]   

print(operacion(sumar_dos, nums))
