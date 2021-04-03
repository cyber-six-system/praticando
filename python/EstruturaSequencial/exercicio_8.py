# -*- coding: utf-8 -*-

""" 
    Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

    Versão do Python em que foi testada: 3.9.2    
"""

__author__ = "Julio Bueno"
__copyright__ = "Copyright 2021, by cyber-six-system"
__credits__ = "Todos desenvolvedores de software livre"
__license__ = "GNU General Public License"
__version__ = "1.0.0"
__maintainer__ = "cyber-six-system"
__status__ = "Prototype"

class Receber:

    def __init__(self, salarioHora, horasTrabalhadas):
        self.salarioHora = self.garantirNumero(salarioHora)
        self.horasTrabalhadas = self.garantirNumero(horasTrabalhadas)
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

    def getTotalRecebimentoMes(self):
        return self.salarioHora * self.horasTrabalhadas

if __name__ == '__main__':
    receberObj = Receber(input(), input())
    totalSalario = receberObj.getTotalRecebimentoMes()
    print("Recebi este mês: R$: %.2f" % totalSalario)