lista = ['1','2','3','4','5','6','7','8']
if not len(lista)%2==0:
    pos = int(len(lista)/2)
    lista[pos]='medio'
else:
    pos = int(len(lista)/2)-1
    lista[pos+4]=lista[pos+3]
    lista[pos+3]=lista[pos+2]
    lista[pos+2]=lista[pos+1]
    lista[pos+1]=lista[pos]
    lista[pos]='medio'
    

print(lista)




#manera profe
mitad = (len(lista) - 1) // 2 #cuando pongo una sopla barra me hace la división contemplando la posibilidad de que tenga decimales y lo trata como float, pero cuando se hace con dos barras se pasa a int truncado
if not len(lista) % 2 == 0:
    pos = int(len(lista)/2)
    
