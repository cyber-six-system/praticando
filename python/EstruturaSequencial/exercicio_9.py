# -*- coding: utf-8 -*-

""" 
    Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e 
    mostre a temperatura em graus Celsius.

    Versão do Python em que foi testada: 3.9.2    
"""

__author__ = "Julio Bueno"
__copyright__ = "Copyright 2021, by cyber-six-system"
__credits__ = "Todos desenvolvedores de software livre"
__license__ = "GNU General Public License"
__version__ = "1.0.0"
__maintainer__ = "cyber-six-system"
__status__ = "Prototype"


class ConversorTemperatura:

    def garantirNumero(self, numero):
        try:
            numero = int(numero)
        except ValueError:
            print('Apenas número!\n')
            while isinstance(numero, str):
                numero = input()
                try:
                    numero = int(numero)
                except ValueError:
                    print('Você inseriu um dado inválido!\n')
                else:
                    return numero
        else:
            return numero
    pass

    def converterFahrenheitParaCelsius(self, fahrenheit):
        fahrenheit = self.garantirNumero(fahrenheit)
        celsius = 5 * ((fahrenheit - 32) /9)
        return celsius

if __name__ == '__main__':
    ctObj = ConversorTemperatura()
    celsius = ctObj.converterFahrenheitParaCelsius(input())
    print('Celsius: %.1f°C' % celsius)