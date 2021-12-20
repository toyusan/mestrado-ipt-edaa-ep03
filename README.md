# Compactação de arquivos com algoritmo de Huffman

---

Tabela de conteúdos
=================
<!--ts-->
   * [Sobre o projeto]
   * [Funcionalidades]
   * [Como executar o projeto]
     * [Pré-requisitos]
     * [Rodando o programa]
	 * [Exemplos de testes]
   * [Autor]
   * [Licença]
<!--te-->

---

## Sobre o projeto

Solução do Exercício Programa 03 da matéria Estrutura de Dados e Analise de Algoritmos do curso de Mestrado em Computação Aplicada do IPT, referente ao 3° Quadrimestre de 2021:

Uma aplicação interessante de árvore binária é a compactação de arquivos usando
os chamados códigos de Huffman. Os códigos de Huffman são códigos binários (atribu
ídos, por exemplo, a caracteres em um texto) de comprimentos variados que são
determinados a partir da frequência de uso de um determinado caractere. A ideia
central é associar números binários com menos bits aos caracteres mais usados em
um texto, possibilitando a sua compactação. O algoritmo de compactação usando
códigos de Huffman tem três fases:

- (1) Cálculo da frequência de cada caractere no texto;
- (2) Execução do algoritmo de Huffman para construção de uma árvore binária
(árvore de Huffman);
- (3) Codificação propriamente dita.

No algoritmo de descompactação usando os códigos de Huffman são necessárias
duas fases:

- (1) Leitura e reconstrução da árvore de Huffman;
- (2) Decodificação propriamente dita.

Para facilitar nosso trabalho podemos considerar pseudo-bits (caracteres 0s e 1s
em vez de bits 0s e 1s).
O algoritmo de Huffman tem como propósito a construção de uma árvore binária
baseada na frequência do uso de letras em um texto. Como exemplo, consideremos
o texto a seguir.

> GNU's Not Unix

Temos que as frequências dos caracteres do texto apresentado como exemplo são:

>'\n': 1, ' ': 2, ''': 1, 'G': 1, 'N': 2, 'U': 2, 'i': 1, 'n': 1, 'o': 1, 's': 1, 't': 1, 'x': 1.

A árvore binária de Huffman será construída de baixo para cima (das folhas para
a raiz), começando a partir das letras menos usadas até atingir a raiz. Em cada
passo do algoritmo, existe uma coleção de árvores de Huffman. No início, cada uma
das letras forma uma árvore que é composta apenas pela raiz e cujo conteúdo é a
frequência com que esta letra ocorre no texto. Em seguida, são escolhidas as duas
árvores com as menores frequências associadas e elas são transformadas em uma
só árvore cujo valor é a soma do valor destas duas. Este processo é repetido até a
alcançar a existência de uma única árvore

>Algoritmo de Huffman

>Entrada: Conjunto C com n caracteres

>Saída: Árvore de Huffman

- 1. Q ← Conjunto de n árvores formadas por nós com os caracteres em C,
e suas respectivas frequências
- 2. para (i = 1; i < n; i + +) faça
- 3. r ← nova raiz
- 4. Filho esquerdo de r ← árvore A1 com frequência mínima em Q,
sendo que A1 deve ser removido de Q
- 5. Filho direito de r ← árvore A2 com frequência mínima em Q,
sendo que A2 deve ser removido de Q
- 6. frequência de r ← soma das frequências de A1 e A2
- 7. retorna árvore Final em Q

A codificação dos caracteres é realizada, associando-se 0 às arestas da árvore de
Huffman que ligam um nó com seu filho esquerdo e 1, às arestas que ligam um nó com
seu filho direito. O código correspondente a cada letra será formado pelo número
binário associado ao caminho da raiz até a folha correspondente. Desta forma, os
códigos resultantes da árvore de Huffman do exemplo são:

- 'x': 000
- '\n': 0010
- ''': 0011
- ' ': 010
- 'G': 0110
- 'i': 0111
- 'N': 100
- 'U': 101
- 'n': 1100
- 'o': 1101
- 's': 1110
- 't': 1111

Desta maneira, o arquivo "descompactado" ficaria (lembre-se que são pseudo-bits):

>01101001010011111001010011011111010101110001110000010

Perceba que para descompactar, basta percorrer a árvore da raiz até uma folha,
obtendo os caracteres.

Considerando o contexto apresentado sua tarefa consiste em implementar um
programa para simular a compactação e descompactação de arquivos de texto. No
caso do processo de compactação o programa deve receber como entrada um arquivo
.txt e devolver como saída o arquivo .txt 'descompactado' (sequência de pseudo-bits
0 e 1). Para descompactar o programa deve receber o arquivo .txt compactado
anteriormente e retornar um arquivo .txt com o texto original.

Durante o processo de compactação deve ser mostrado na tela para o usuário: 
- (1) a frequência dos caracteres do texto; 
- (2) a árvore de Huffman obtida pelo algoritmo(percurso pré-ordem estudado na disciplina), e 
- (3) sequência de pseudo-bits do texto compactado."

---

## Funcionalidades

>- O usuário entra com o caminho do arquivo de teste contendo o texto a ser compactado, conforme o enunciado. O nome do arquivo deve ser necessariamente <b>texto_para_compactar.txt</b>;

>- O software realiza a leitura do arquivo e determina a frequência de caracteres lidos, apresentando ao usuário;

>- Em seguida, o software monta a árvore binária de Huffman, e a apresenta, em pré-ordem ao usuário;

>- Na sequência, o software apresenta ao usuário a sequência de pseudo código binário, resultante da compactação;

>- Por fim, o software salva um novo arquivo, no mesmo endereço fornecido pelo usuário, com o nome de <b>texto_compactado.txt</b>, contendo o pseudo código binário resultante.

>- Na segunda parte, o software abre o arquivo compactado, realiza a descompactação e salva o resultado no mesmo caminho fornecido pelo usuário, com o nome de <b>texto_descompactado.txt</b>
---

## Como executar o projeto

### Pré-requisitos

* [Python 3.8.7](https://www.python.org/downloads/release/python-387/);
 
#### Rodando o programa

> Colocar os três arquivos no mesmo diretório:

>- ep03.py 
>- huffmanTree.py 
>- node.py 
>- texto_para_compactar.txt

> Localizar o arquivo ep03.py e clicar duas vezes para abri-lo;

> Digitar o caminho do arquivo contendo o texto a ser compactado (<b>texto_para_compactar</b>);

> Pressionar enter para iniciar o processo de compactaç. 

#### Exemplo de teste

- Conteúdo do arquivo teste.txt:

><b>GNU's Not Unix</b>

Ao iniciar o programa, entrar com o endereço do diretório com o arquivo para compactar, por exemplo:

><b>Entre com o arquivo para compactar:</b> 
D:\Workspace 

><b>Frequência de caracteres do texto</b>: Counter({'N': 2, 'U': 2, ' ': 2, 'G': 1, "'": 1, 's': 1, 'o': 1, 't': 1, 'n': 1, 'i': 1, 'x': 1, '\n': 1})

><b>Árvore de Huffman obtida pelo algortimo em Pré Ordem:</b> 
('+', 15, (('+', 7, (('+', 3, (('G', 1, (None, None)), (' ', 2, (None, None)))), ('+', 4, (('U', 2, (None, None)), ('N', 2, (None, None)))))), ('+', 8, (('+', 4, (('+', 2, (('\n', 1, (None, None)), ('x', 1, (None, None)))), ('+', 2, (('i', 1, (None, None)), ('n', 1, (None, None)))))), ('+', 4, (('+', 2, (('t', 1, (None, None)), ('o', 1, (None, None)))), ('+', 2, (('s', 1, (None, None)), ("'", 1, (None, None))))))))))


><b>Sequência de pseudo-bits do texto compactado: </b>00001101011111110001011110111000010101011101010011000

><b>Arquivo 'texto_compactado.txt' salvo em </b>D:\Workspace

><b>Iniciando o processo de descompactação do arquivo. Abrindo arquivo 'texto_compactado.txt...</b>

><b>Código compactado:</b>  00001101011111110001011110111000010101011101010011000

><b>Texto descompactado:</b>  GNU's Not Unix


><b>Arquivo 'texto_descompactado.txt' salvo em</b> D:\Workspace 


---

### Autor 

- Airton Y. C. Toyofuku
- airton.toyofuku@gmail.com

---
### Licença
Este projeto esta sob a licença [MIT](./LICENSE).

