from clases import Vehiculo,coche
# coche1 = Vehiculo('Tesla')
# nuevoCoche = coche('Audi')
# coche1.mover()
# nuevoCoche.mover()
# print(coche1.marca)
coches = [coche('Tesla', 'Roadster','Verde')]
for coche in coches:
    if coche.marca == 'Tesla':
        print('Tesla ENCONTRADO')
        print(coche)
    print(coche.marca, coche.modelo, coche.color)