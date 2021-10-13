from typing import List


list = ['cero','uno','dos','tres']
list.append('ultimo') #AÑADE UN ELEMENTO A LA LISTA
list.remove('ultimo') #ELIMINA EL PRIMER ELEMENTO QUE SEA COMO EL QUE LE INDIQUEMOS, PERO SI NO ESTÁ CASCA
print(list)
if 'uno' in list:
    print('Está')

elemento_borrado = list.pop()#ELIMINA EL ÚLTIMO ELEMENTO Y TE DEVUELVE EL ELEMENTO, A NO SER QUE RECIBA UN PARÁMETRO Y TE BORRARÍA LA POSICIÓN DE ESE ELEMENTO
#BORRAR UNA LISTA COMPLETA
list.clear()
