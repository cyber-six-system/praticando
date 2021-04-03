# -*- coding: utf-8 -*-

""" 
    Faça um Programa que converta metros para centímetros.

    Versão do Python em que foi testada: 3.9.2    
"""

__author__ = "Julio Bueno"
__copyright__ = "Copyright 2021, by cyber-six-system"
__credits__ = "Todos desenvolvedores de software livre"
__license__ = "GNU General Public License"
__version__ = "1.0.0"
__maintainer__ = "cyber-six-system"
__status__ = "Prototype"

class Centimetros:

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

    def ConverterMetrosEmCentimetros(self, metros):
        metros = self.GarantirNumero(metros)
        return metros * 100
    pass

if __name__ == '__main__':
    centimetrosObj = Centimetros()
    metrosInformado = input('Metros >> ')
    metrosEmCentimetros = centimetrosObj.ConverterMetrosEmCentimetros(metrosInformado)
    print("Conversão para Centímetros: %dcm" % float(metrosEmCentimetros))