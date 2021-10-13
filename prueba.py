# print("klk")
# while True:
#     print("hola")
# variable = 1
# numero = 12
# print(type(variable)) # PARA SABER EL TIPO DE VARIABLE 
# print(variable)

# variable = 'Hola' + str(numero)

# variable = f'Hola {numero * 2} - {numero}' #solo funciona a partir de la 3.6

# # if True:
# #     print('Dentro del if')

# if 5 < 10 and 12 > 10:
#     print('YEAH')


# if not variable==2:
#     print('negaoooooo')

# while numero < 15:
#     print(numero)
#     numero += 1

# while variable < 5 :
#     variable += 1
#     if variable == 3:
#         break

# while variable < 5 :
#     variable += 1
#     if variable == 3:
#         continue

# while variable < 5:
#     pass

try:
    dato = input("Introduce un numero: ")
    dato = int(dato)
    print(f'El dato introducido es: {dato * 2}') #forma de concatenar sin usar el +
except Exception as e: #Para no confundir las excepciones con las interrupciones
    print(str(e))
    print('Inutil, te he dicho que introduzcas un numero.')

try:
    raise Exception('Otro error')
    dato = input("Introduce un numero: ")
    dato = int(dato)
    print(f'El dato introducido es: {dato * 2}') #forma de concatenar sin usar el +
except Exception as e: #Para no confundir las excepciones con las interrupciones
    print(str(e))
    print('Inutil, te he dicho que introduzcas un numero.')


try:
    dato = input("Introduce un numero menor que 10: ")
    dato = int(dato)
    if dato >= 10:
        raise Exception('Número fuera de rango')
    print(f'El dato introducido es: {dato * 2}') #forma de concatenar sin usar el +
except ZeroDivisionError: #Para no confundir las excepciones con las interrupciones
    print("Un 0 no!!!!")
    print('Inutil, te he dicho que introduzcas un numero.')