#TUPLAS - listas que no se pueden modificar
tupla = ('Enero','Febrero','Diciembre')
print(tupla)
print(tupla[1])
for mes in enumerate(tupla):
    print(mes)

#REHACER LA DUPLA
lista_meses = []
for mes in tupla:
    lista_meses.append(tupla)

lista_meses[1]='Junio'
tuplaNueva = tupla(lista_meses)

#FORMA RAPIDA SERÍA CASTEAR LA TUPLA COMO LISTA AÑADIR/MODIFICAR EL ELMENTO Y VOLVERLA A CASTEAR COMO TUPLA