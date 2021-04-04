# -*- coding: utf-8 -*-

""" 
    Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
        1º o produto do dobro do primeiro com metade do segundo .
        2º a soma do triplo do primeiro com o terceiro.
        3º o terceiro elevado ao cubo.


    Versão do Python em que foi testada: 3.9.2    
"""

__author__ = "Julio Bueno"
__copyright__ = "Copyright 2021, by cyber-six-system"
__credits__ = "Todos desenvolvedores de software livre"
__license__ = "GNU General Public License"
__version__ = "1.0.0"
__maintainer__ = "cyber-six-system"
__status__ = "Prototype"

class ValidarNumero:

    def garantirNumeroInteiro(self, numero, text):
        try:
            numero = int(numero)
        except ValueError:
            print('Apenas número!\n %s' % text)
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

    def garantirNumeroReal(self, numero, text):
        try:
            numero = int(numero)
        except ValueError:
            print('Apenas número!\n %s' % text)
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

global PRIMEIRA_SOLUCAO_STR, SEGUNDA_SOLUCAO_STR, TERCEIRA_SOLUCAO_STR

PRIMEIRA_SOLUCAO_STR =  "O produto do dobro do primeiro com metade do segundo: "
SEGUNDA_SOLUCAO_STR =  "A soma do triplo do primeiro com o terceiro: "
TERCEIRA_SOLUCAO_STR =  "o terceiro elevado ao cubo: "

class MyInputs(object):

    def numOneIntGet(self):
        return self.__numOneInt

    def numOneIntSet(self, numOneInt):
        text = "Primeiro numero (int) >> "
        self.__numOneInt = ValidarNumero().garantirNumeroInteiro(numOneInt, text)
    
    def numTwoIntGet(self):
        return self.__numTwoInt

    def numTwoIntSet(self, numTwoInt):
        text = "Segundo numero (int) >> "
        self.__numTwoInt = ValidarNumero().garantirNumeroInteiro(numTwoInt, text)
    
    def numThreeRealGet(self):
        return self.__numThreeReal

    def numThreeRealSet(self, numThreeReal):
        text = "Terceiro numero real >> "
        self.__numThreeReal = ValidarNumero().garantirNumeroReal(numThreeReal, text)
        

class Logica:

    def __init__(self, MyInputsModel):
        self.__numOneInt = MyInputsModel.numOneIntGet()
        self.__numTwoInt = MyInputsModel.numTwoIntGet()
        self.__numThreeReal = MyInputsModel.numThreeRealGet()

    def produtoDoDobroPrimeiroComMetadeDoSegundo(self):
        return self.__numOneInt * 2 + (self.__numTwoInt / 2)
    
    def somaTriploDoPrimeiroComTerceiro(self):
        return (self.__numTwoInt * 3) + self.__numThreeReal
    
    def terceiroValorElevadoAoCubo(self):
        return self.__numThreeReal ** 3

if __name__ == '__main__':
    myInputsModel = MyInputs()
    myInputsModel.numOneIntSet(input("Primeiro numero (int) >> "))
    myInputsModel.numTwoIntSet(input("Segundo numero (int) >> "))
    myInputsModel.numThreeRealSet(input("Terceiro numero (Real) >> "))
    logicaObj = Logica(myInputsModel)

    print(PRIMEIRA_SOLUCAO_STR+' %d' % logicaObj.produtoDoDobroPrimeiroComMetadeDoSegundo())
    print(SEGUNDA_SOLUCAO_STR+' %.2f' % logicaObj.somaTriploDoPrimeiroComTerceiro())
    print(TERCEIRA_SOLUCAO_STR+' %.2f' % logicaObj.terceiroValorElevadoAoCubo())