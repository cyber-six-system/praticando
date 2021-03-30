# -*- coding: utf-8 -*-

""" 
    Faça um Programa que peça as 4 notas bimestrais e mostre a média.

    Versão do Python em que foi testada: 3.9.2    
"""

__author__ = "Julio Bueno"
__copyright__ = "Copyright 2021, by cyber-six-system"
__credits__ = "Todos desenvolvedores de software livre"
__license__ = "GNU General Public License"
__version__ = "1.0.0"
__maintainer__ = "cyber-six-system"
__status__ = "Prototype"

def isNum(x):
    """
        Titulo:
            É número? 

        Descrição:
            Verificar se dado que entrou é número

            Este método também é responsável por validar que tipo de informação o usuário inseriu, 
            se de fato é númerico.

        Parâmetros:
            :param x: int 
                Variável inteira para tratamento da validação
            :return Str
        """
    while not x.isnumeric():
            x = input("Digite um número: ")
            
    return "número %d foi informado!" % int(x)

print(isNum(input()))
