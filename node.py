########################################################################################################################
# @file     node.py
# @author   Airton Yassushiko Coppini Toyofuku
# @date     17/12/2021
# @brief    Classe node correspondente aos nós da arvore binária
########################################################################################################################

class Node:

########################################################################################################################
#  @brief  Construtor da classe Node
#  @param  conteudo: valor do conteudo do node
#  @param  frequencia: valor da frequencia do node
#  @param  esquerda: valor da esquerda do node
#  @param  direita: valor da direita do node
#  @retval None
    def __init__(self, conteudo, frequencia, esquerda, direita, binario = ''):
        self.conteudo = conteudo
        self.frequencia = frequencia
        self.esquerda = esquerda
        self.direita = direita
        self.binario = binario

########################################################################################################################
#  @brief  retorna se o node é uma folha ou nao
#  @retval True se é folha, False se não é folha
    def ehFolha(self):
        return self.esquerda == None and self.direita == None

########################################################################################################################
#  @brief  Sobrescreve o metodo de apresentacao do objeto
    def printRepresentacaoBinaria(self):
        return repr((self.conteudo, self.binario))

########################################################################################################################
#  @brief  Sobrescreve o metodo de apresentacao do objeto
    def __repr__(self):
        return repr((self.conteudo , self.frequencia,(self.esquerda, self.direita)))




