
import string


class Automovil:

    def __init__(self, modelo, marca, color):
        self.modelo = modelo
        self.marca = marca
        self.color = color
        self.estado = 'en reposo'
        self._motor = Motor(cilindros=4)
        

    def acelerar(self, tipo: str= 'despacio'):
        if tipo == 'rapida':
            self._motor.inyecta_gasolina(10)
            print('vas rapido')
        else:
            self._motor.inyecta_gasolina(3)
            print('vas lento')
        self._estado = 'en movimiento'


class Motor:
    
    def __init__(self, cilindros: int, tipo: str= 'gasolina',nivelGasolina = 111):
        self.cilindros = cilindros
        self.tipo = tipo
        self._temperatura = 0
        self.nivelGasolina = nivelGasolina

    def inyecta_gasolina(self, cantidad: int):
        self.nivelGasolina = self.nivelGasolina - cantidad
        print (f'el nivel de gasolina es {self.nivelGasolina}')

if __name__ == '__main__':
    car = Automovil(3,'mazada','rojo')
    car.acelerar("lenta")
    car.acelerar('rapida')
    car.acelerar('lenta')