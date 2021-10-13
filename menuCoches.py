#Scrip que pregunta marca, modelo y coche, posteriormente guardar esos datos.
import os
from vehiculos import Coche

path_base = os.path.dirname(os.path.abspath(__file__))
exit = "1"
lista = []
with open(f"{path_base}/coches.txt","r", encoding='UTF-8') as archivo:
    for coche in archivo.readlines():
        listaCoche = coche.split(" ")
        print(listaCoche)
        dicCoche = {
            'marca' : listaCoche[0],
            'modelo' : listaCoche[1],
            'color' : listaCoche[2].replace("\n","")
        }
        lista.append(dicCoche)
archivo.close()
print(lista)



while exit !="0" :
    with open(f"{path_base}/coches.txt","a", encoding='UTF-8') as archivo:
        print('\n¿Cuál es la marca del vehículo?')
        marcaDato = input()
        print('\n¿Cuál es el modelo del vehículo?')
        modeloDato = input()
        print('\n¿Cuál es el color del vehículo?')
        colorDato = input()
        coche = Coche(marcaDato,modeloDato,colorDato)
        archivo.write(f'\n{coche.marca} {coche.modelo} {coche.color}')
        print('\nCoche guardado correctamente\n¿Desea introducir otro coche?1(Si)/0(No)')
        exit = input()
    archivo.close()
        

