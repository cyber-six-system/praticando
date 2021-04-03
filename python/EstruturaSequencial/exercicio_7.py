# -*- coding: utf-8 -*-

""" 
    Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

    Versão do Python em que foi testada: 3.9.2    
"""

__author__ = "Julio Bueno"
__copyright__ = "Copyright 2021, by cyber-six-system"
__credits__ = "Todos desenvolvedores de software livre"
__license__ = "GNU General Public License"
__version__ = "1.0.0"
__maintainer__ = "cyber-six-system"
__status__ = "Prototype"

class Quadrado:

    def __init__(self, base, altura):
        self.base = self.garantirNumero(base)
        self.altura = self.garantirNumero(altura)
    pass

    def garantirNumero(self, numero):
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

    def calcularAreaQuadradoEmDobro(self):
        return (self.base * self.altura)*2


if __name__== '__main__':
    quadradoObj = Quadrado(input(), input())
    dobroDaArea = quadradoObj.calcularAreaQuadradoEmDobro()
    print("Dobra da àrea do quadrado: %d" % dobroDaArea)