# -*- coding: utf-8 -*-

""" 
    Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

    Versão do Python em que foi testada: 3.9.2    
"""

__author__ = "Julio Bueno"
__copyright__ = "Copyright 2021, by cyber-six-system"
__credits__ = "Todos desenvolvedores de software livre"
__license__ = "GNU General Public License"
__version__ = "1.0.0"
__maintainer__ = "cyber-six-system"
__status__ = "Prototype"

import math

class Circulo:
    
    def GarantirNumero(self, numero):
        try:
            numero = float(numero)
        except ValueError:
            print('Apenas número!\n')
            while isinstance(numero, str):
                numero = input()
                try:
                    numero = float(numero)
                except ValueError:
                    print('Você inseriu um dado inválido!\n')
                else:
                    return numero
        else:
            return numero
    pass

    def CalcularAreaCirculo(self, raio):
        raio = self.GarantirNumero(raio)
        return (raio**2)*math.pi
    pass

if __name__ == ('__main__'):
    circuloObj = Circulo()
    capturarRaio = input("Informe o raio do cículo >> ")
    area = circuloObj.CalcularAreaCirculo(capturarRaio)
    print("A área do circulo é: %.2f" % area)