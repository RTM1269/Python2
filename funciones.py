
# def sumar(valor1,valor2):
#     print('Resultado= ',valor1+valor2)

# sumar(2,4)
#primero VAN LOS QUE NO TIENEN VALOR POR DEFECTO --> LOS OBLIGATORIOS  Y DESPUES LOS QUE SI TIENEN VALOR POR DEFECTO 
# def sumar(valor1=0,valor2=0):
#       return valor1+valor2
# def sumar(valor1,valor2,*numeros):
# def sumar(*numeros):
#     # resultado = valor1+valor2
#     resultado = 0
#     for numero in numeros:
#         resultado += numero
#     return resultado

 
# result = sumar(2,5,8)
# print(result)

def factorial(numero):
    resultado = 1
    while numero>0:
        resultado *= numero
        numero -= 1
    return resultado
print(factorial(4))

def factorial_recursivo(numero):
    if numero < 0:
        raise Exception('Número negativo no permitido')
    if numero == 0:
        return 1
    return numero * factorial_recursivo(numero-1)
print(factorial_recursivo(-1))