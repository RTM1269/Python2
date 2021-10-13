
class Vehiculo:
    
    def __init__(self, marca): #SIEMPRE SE DEBE PASAR self PARA CREAR EL METODO, YA QUE ES EL MISMO(AUNQUE NO ES NECESARIO A LA HORA DE CREAR UNA INSTANCIA)
        self.marca = marca
        self.odometro = 0
    
    def mover(self, kilometros):
        self.odometro += kilometros
        print(f'Moviendo el vehículo {self.marca} {self.odometro} km')


class Coche(Vehiculo): #Para crear herencia se utilizan ('nombre de la clase padre')//PUEDE HEREDAR DE VARIOS PADRES

    def __init__(self, marca, modelo, color):
        super().__init__(marca)
        self.modelo = modelo
        self.color = color
    
    def __str__(self):
         return f'({self.marca}) ({self.color}) ({self.modelo})'

    def __repr__(self) -> str:
        return super().__repr__()
    
    