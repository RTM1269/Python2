lista = ['cero', 'uno', 'dos', 'tres', 4]

print(lista[0])
print(lista[-1])#para la última posicion
print(len(lista)-1)#para la última posicion

print(lista[2:5])#intervalo de la lista
print(lista[2:])#desde la posición 2 hasta el final
print(lista[:2])#desde el principio hasta el final

#forma lenta/antigua
cont = 0
max_lenght = len(lista)
while cont < max_lenght:
    print(lista[cont])
    cont += 1

#forma rápida/proo
# for item in lista:
#     print(item, end = ' - ')

for i in range(len(lista)):
    print(f'{i} -> {lista[i]}')

