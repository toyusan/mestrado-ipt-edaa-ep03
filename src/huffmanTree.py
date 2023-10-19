########################################################################################################################
# @file     arvore.py
# @author   Airton Yassushiko Coppini Toyofuku
# @date     17/12/2021
# @brief    Classe arvore
########################################################################################################################

class HuffmanTree:
    import node

########################################################################################################################
#  @brief  Apresenta a arvore em pre ordem
#  @param  Node: Raiz da arvore
#  @retval None
    def preOrdem(self, node):
        print(node)

        #if (node == None):
        #    return
        #print(node)
        #if(node.esquerda):
        #    self.preOrdem(node.esquerda)
        #if(node.direita):
        #    self.preOrdem(node.direita)

########################################################################################################################
#  @brief  Atribui a cada node da arvore uma codificação binaria
#  @param  Node: Raiz da arvore
#  @retval None
    def codificaBinario(self, node):

        if node == None:
            return

        # sempre que for para a esquerda, concatena '0' ao node
        if node.esquerda != None:
            node.esquerda.binario = str(node.binario) + '0'
            self.codificaBinario(node.esquerda)

        # sempre que for para a direita, concatena '1' ao node
        if node.direita != None:
            node.direita.binario = str(node.binario) + '1'
            self.codificaBinario(node.direita)

        return

########################################################################################################################
#  @brief  Compacta o texto com base na arvore gerada
#  @param  node: Raiz da arvore
#  @param  texto: Texto a ser compactado
#  @retval None
    def compacta(self, node, texto):
        codigo_binario = ''

        # Percorre a arvore em busca do código binario correspondente e
        for letra in texto:
            codigo_binario = codigo_binario + str(self.getCodigoFolha(node, letra))

        return codigo_binario

########################################################################################################################
#  @brief  Funçãoo interna para devolver o código binario da folha
#  @param  node: Raiz da arvore
#  @param  letter: letra a ser procurada na arvore
#  @retval None
    def getCodigoFolha(self, node, letra):  # procura um dado caractere na árvore e retorna seu código

        codigo_binario = ''

        # Achou a letra e retorna o codigo binario dela
        if node.conteudo == letra:
            return node.binario

        # Verifica o filho esquerdo é a folha que procuramos
        else:
            if (node.esquerda):
                codigo_binario = self.getCodigoFolha(node.esquerda, letra)

            # Se nao achou, verifica no filho direito
            if codigo_binario == '' and node.direita:
                codigo_binario = self.getCodigoFolha(node.direita, letra)

        return codigo_binario

########################################################################################################################
#  @brief  Descompacta o texto com base na arvore gerada
#  @param  node: Raiz da arvore
#  @param  texto: Texto a ser descompactado
#  @retval None
    def descompacta(self, raiz, texto_compactado):
        no_arvore = raiz
        texto_descompactado =''

        for binario in texto_compactado:

            # Verifica se vai para a esquerda ou para a direita
            if binario == '0':
                no_arvore = no_arvore.esquerda
            else:
                no_arvore = no_arvore.direita

            # Se for uma folha, pega o conteudo dela e volta para a raiz
            if(no_arvore.ehFolha()):
                texto_descompactado = texto_descompactado + str(no_arvore.conteudo)
                no_arvore = raiz

        return texto_descompactado

########################################################################################################################
#  @brief  Apresenta as folhas da arvore com o seu código binario - apenas para debug
#  @param  Node: Raiz da arvore
#  @retval None
    def imprimeFolha(self, node):
        if (node == None):
            return
        if (node.esquerda):
            self.imprimeFolha(node.esquerda)
        if(node.ehFolha()):
            print(node.printRepresentacaoBinaria())
        if (node.direita):
            self.imprimeFolha(node.direita)