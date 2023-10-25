########################################################################################################################
# @file     ep03.py
# @author   Airton Yassushiko Coppini Toyofuku
# @date     17/12/2021
# @brief    Solução do Exercício Programa 03 da matéria Estrutura de Dados e Analise de Algoritmos do curso de Mestrado
#           em Computação Aplicada do IPT, referente ao 3° Quadrimestre de 2021:
########################################################################################################################

########################################################################################################################
#  @brief  Abre o arquivo de teste e retorna as linhas lidas em uma lista
#  @param  address: endereco do arquivo
#  @param  mode: modo e abertura do arquivo
#  @retval linhas lidas do arquivo
def openFile(address):
    try:
        file = open(address, 'r')
        texto = file.read()
    except:
        print("Erro ao abrir o arquivo")
    finally:
        file.close()
    return texto

########################################################################################################################
#  @brief  Salva um arquivo
#  @param  address: endereco do arquivo
#  @param  texto: texto a ser escrito no arquivo
#  @retval None
def saveFile(address, texto):
    try:
        file = open(address,'w')
        file.write(texto)
    except:
        print("Erro ao salvar o arquivo")
    finally:
        file.close()
    return

########################################################################################################################
#  @brief  Algoritmo de Huffman para montar a arvore
#  @param  C: Conjunto de n árvores formadas por nós com os caracteres em C, e suas respectivas frequências
#  @retval Árvore de Huffman
def huffman(C,tamanho_lista_nodes):
    Q = C
    i = 0
    #print("Q = " + str(Q))
    for i in range(1, tamanho_lista_nodes, 1):

        r = node.Node('+', None, Q[0], Q[1])
        r.frequencia = Q[0].frequencia + Q[1].frequencia

        # Removendo o A1 e A2 de Q
        Q.remove(Q[1])
        Q.remove(Q[0])

        # Inserindo a nova arvore no conjunto e ordenando por frequencia
        Q.append(r)
        Q.sort(key = lambda x: x.frequencia)
        #print("Q = " + str(Q))

    return Q

########################################################################################################################

print("=============================================================")
print("=     Compactação de arquivos com algoritmo de Huffman      =")
print("=============================================================")

from collections import Counter
import node
import huffmanTree

# Entrando com o endereço do arquivo
addressInput = input("Entre com o arquivo para compactar: ")

#Escolhendo o diretório onde será salvo o texto compactado e descompactado
addressOutput = input("Digite o diretório onde será salvo o arquivo: ")


# Abre o arquivo no modo leitura (r)
texto = openFile(addressInput + "/texto_para_compactar.txt")

print("\r\nIniciando o processo de compactacao do arquivo 'texto_para_compactar.txt'...")

# Determinando a frequencia de caracteres
counter = Counter(texto)
print("\r\nFrequência de caracteres do texto: " + str(counter))

# Criando uma lista de nodes com os caracteres em ordem crescente de suas frequencias
lista_nodes =[]
tamanho_lista_nodes = 0
for item, count in reversed(counter.most_common()):
    novo_node = node.Node(item, count, None, None)
    lista_nodes.append(novo_node)
    tamanho_lista_nodes = tamanho_lista_nodes + 1

# Cria a árvore de Huffman
raiz = huffman(lista_nodes,tamanho_lista_nodes)
arvore_huffman = huffmanTree.HuffmanTree()
print("\r\nÁrvore de Huffman obtida pelo algortimo em Pré Ordem: ")
arvore_huffman.preOrdem(raiz[0])

# Atribuindo os valores das arestas e determinando o codigo binario resultante da arvore
arvore_huffman.codificaBinario(raiz[0])

# Atribuindo os códigos binarios as letras no texto
texto_compactado = arvore_huffman.compacta(raiz[0], texto)
print("\r\nSequência de pseudo-bits do texto compactado: " + texto_compactado)

# Salvando arquivo com o conteudo compactado
#addressOutput = input("Digite o diretório onde será salvo o arquivo: ")
saveFile(addressOutput + "/texto_compactado.txt", texto_compactado)
print("\r\nArquivo 'texto_compactado.txt' salvo em " + addressOutput)


# Iniciando o processo de descompactacao
print("\r\n=============================================================")

print("\r\nIniciando o processo de descompactação do arquivo. Abrindo arquivo 'texto_compactado.txt...")
#addressOutput = addressOutput + "/texto_compactado.txt"

texto_compactado = openFile(addressOutput + "/texto_compactado.txt")
print("\r\nCódigo compactado: " + texto_compactado)

texto_descompactado = arvore_huffman.descompacta(raiz[0], texto_compactado)
print("\r\nTexto descompactado: " + texto_descompactado)

#addressOutput = input("Digite o diretório onde será salvo o arquivo: ")
saveFile(addressOutput + "/texto_descompactado.txt", texto_descompactado)
print("\r\nArquivo 'texto_descompactado.txt' salvo em " + addressOutput)

print("=============================================================")

saida = input("> Precione enter para sair...")