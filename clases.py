class Vehiculo:
    def __init__(self,marca):  #CONSTRUCTOR   -   A CUALQUIER MÉTODO HAY QUE PASARLE EL PROPIO OBJETO NORMALMENTE this, AQUI self
        self.marca = marca    #IGUAL QUE EN JavaScript si no existe lo crea y si existe lo reasigna
    def mover(self):
        print(f'Moviendo el vehículo {self.marca}')

class coche(Vehiculo):  #la clase coche HEREDA de Vehiculo (AUNQUE PUEDE HEREDAR DE VARIAS CLASES)
    def __init__(self,marca,modelo,color):  
        super().__init__(marca) 
        self.modelo = modelo
        self.color = color
