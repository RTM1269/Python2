#COMO UN JSON
coche = {
    'marca': 'Tesla',
    'modelo': 'Roadster 2020',
    'color': 'Rojo',
    'ruedas': 4,
    'puertas': 2
}
tesla = {
    'marca': 'Tesla',
    'modelo': 'Roadster 2020',
    'color': 'Rojo',
    'ruedas': 4,
    'puertas': 2
}
ford = {
    'marca': 'Ford ',
    'modelo': 'focus',
    'color': 'Gris',
}
coches = [ford,tesla]#FORMATO LISTA

#AVERIGUO DONDE SE ENCUENTRA EL DICCIONARIO A ACTUALIZAR/MODIFICAR
for coche in coches:
    if coche['marca'] == 'Tesla':
        coche['color']='Azul'
        print(coche)
        break

# print(coche['marca'])#SE ACCEDE A LOS VALORES POR LAS KEYS 

# #imprimir todo el diccionario
# for clave in coche:
#     print(clave,coche[clave])

# valores = list(coche.values())
# keys = list(coche.keys())
# print('VALORES',valores,'\n CLAVES',keys)

# #UPDATE - SI está te lo ACTUALIZA y si no está te lo AÑADE  
# coche.update({'llaves':2,'color':'Verde'})
# print(coche)
# contro = coche.pop('llaveswss',None)#le digo que me elimine LLAVES, y si no existe me envie el segundo valor que tendré que recoger en una variable
# print(contro)