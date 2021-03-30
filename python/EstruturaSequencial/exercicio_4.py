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

class CalculaMedia:

    global MSG
    
    MSG = "Digite apenas número:" 

    """
        :param_global MSG: str
            Mensagem fixa para exibição quando houver falha na validação
    """

    def adicionaAcumulo(self, a, x):
        """
        Titulo:
            Somar ao acumulado

        Descrição:
            Pega o dado (x) do usuário e soma ao acumulado (a)

            Este método também é responsável por validar que tipo de informação o usuário inseriu, 
            se de fato é númerico independente do seu tipo ou se é uma string.

            Se caso for string forçará ao usuário inserir um número!

        Parâmetros:
            :param a: float 
                Variável para acumuluar a soma do resultado
            :param x: float 
                Novo dado inserido pelo usuário
            :return float
        """

        try:
            #Tentar converter as variáveis para o tipo float
            a, x = float(x), float(a)
        #Se houver falha?
        except ValueError: 
            #Valida se o usuário inseriu uma string
            while isinstance(x, str): 
                #Pede ao usuário nova inserção
                x = input() 
                try:
                    #Tentar forçar a conversão para float a nova inserção 
                    x = float(x)
                except ValueError: 
                    #Caso der problema de novo, exibit a mensagem fixa e volta o ciclo do método
                    print(MSG)
                else: 
                    #Caso usuário inserir corretamente adiciona x(entrada) ao a(acumulo) e retorna
                    return a+x
        else:
            #Caso usuário de primeira inserir corretamente adiciona x(entrada) ao a(acumulo) e retorna
            return a+x
    pass

    def calculoMedia(self, x):
        """
        Titulo:
            Calcular a média
    
        Descrição:
            Com base no montante passado por parâmetro, este será dividido por 4, e é o resultado mediano.

        Parâmetro:
            :param x: float
                Valor que passará para este método preferencialmente que seja do tipo float
        """

        #Dividirá o valor x por 4, como pede o enunciado na descrição
        return x/4
    pass

    def mediaAnual(self):
        """
        Titulo:
            Média Anual

        Descrição
            Executar a inserlçao dos 4 dados de notas e calcular a média no final

        Parâmetros:
            :param x: int
                Serve como contator apenas e seu valor inicial é 0
            :param a: float 
                Variável principal para a execução do programa, é esta que acumula o saldo total das notas
            :return float
        """
        x = 0
        a: float = 0.0

        #Se faz necessário esse loop para certificar de que irá entrar apenas 4 notas
        while x < 4:
            #Trexo crucial, chama o método passando o valor já acumulado e a entrada do usuário para somar
            a = self.adicionaAcumulo(a, input()) 
            x+=1
        #Ultima operação do sistema, aqui é feito de fato o cálculo e retorna
        return float(self.calculoMedia(a))
    pass

if __name__ == '__main__':
    """
    Titulo:
        Main()

    Descrição:
        Ponto de partida para a execução do programa.
    """
    cm = CalculaMedia()
    print("Média Bimestral: %.2f " % cm.mediaAnual())
    """
    1º passo: 
        Primeiro executa a operação do enunciado

    2º Passo: 
        Com o retorno do resultado, aloca na memória 

    3º Passo: 
        Concatena o resultado formatando-o com apenas 5 casas decimais com a String
    """