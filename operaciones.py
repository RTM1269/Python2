#primera manera
import multiplicadora as m #importamos con el nombre del archivo sin el .py
#forma en python de tener un main
if __name__ == '__main__':
    print(m.suma(5,6))

#segunda manera
from multiplicadora import suma,resta
print(resta(10,5))
print(f'operaciones.py --> {__name__}')