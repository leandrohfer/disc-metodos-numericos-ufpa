"""
    Trabalho 2 de Métodos Numéricos

    @autor Leandro_Henrique

"""

# Importação da biblioteca Numpy para a manipulação de Arrays
import numpy as np

#########################################################################



#########################################################################



#########################################################################

# Leitura do arquivo "dados.txt" para salvá-lo como uma matriz de N linhas
# e 2 colunas


with open('dados.txt', 'r') as dados:
    # Leitura do arquivo "dados.txt" e salvando ele como uma string
    matriz1 = dados.read()

    # Divisão da string em função dos espaços entre os números e
    # posteriormente salvando esses dados em uma lista de valores
    # do tipo string
    matriz2 = matriz1.split()

    # Transformação da lista de strings para um array NP padrão
    matriz2 = np.array(matriz2)

    # Declaração de uma variável auxiliar para o nº de linhas do array NP
    aux = int((len(matriz2)) / 2)

    # Modificação do formato do array NP para uma matriz Nx2
    matrizArrayNP = matriz2.reshape(aux, 2)

    # Transformação de todos os valores desta matriz para o tipo Float
    # para podermos fazer cálculos com esses valores
    matrizFinal = np.float_(matrizArrayNP)

#########################################################################

# Exibição da Matriz final obtida a partir de "dados.txt" e dos valores
# de DeltaX e do número de Linhas da Matriz final

linha = '-' * 50

print(linha)
print('Matriz contida dentro do arquivo dados.txt: \n')
print(matrizArrayNP)
print('\n'+linha+'\n')

dx = matrizFinal[1][0] - matrizFinal[0][0]
print('Valor do DeltaX deste dataset: ', dx)
print('\n'+linha+'\n')

ultimoIndice = len(matrizFinal) - 1
print('Este dataset é uma matriz com', ultimoIndice, 'linhas.')
print('\n'+linha+'\n')

#########################################################################

# print('Escolha o tipo de operação desejado.')
# tipo = int(input('Digite [1] para derivada ou [2] para integral: '))

# if tipo == 1:

#     # Criação do arquivo "derivada.txt" contendo os resultados obtidos a
#     # partir da chamada das funções definidas

#     with open('derivada.txt', 'a+') as derivada:

#         # Laço para escrever o mesmo número de linhas que "dados.txt" contém
#         for i in range(len(matrizFinal)):

#             # Escrevendo os mesmos valores de X
#             derivada.write(str(matrizFinal[i][0])+' ')

#             # Laços para a definição de que diferença usar dependendo da
#             # posição do índice
#             if i == 0:
#                 derivada.write(str(diferencaAvancada()) + '\n')
#             elif i == ultimoIndice:
#                 derivada.write(str(diferencaAtrasada()) + '\n')
#             else:
#                 derivada.write(str(diferencaCentrada(i)) + '\n')
# elif tipo == 2:

#     # Criação do arquivo "integral.txt" contendo os resultados obtidos a
#     # partir da chamada da função definida

#     with open('integral.txt', 'a+') as integral:

#         # Laço para escrever o mesmo número de linhas que "dados.txt" contém
#         for i in range(len(matrizFinal)):

#             # Escrevendo os mesmos valores de X
#             integral.write(str(matrizFinal[i][0])+' ')

#             # Laços para a definição de que no primeiro parâmetro da integral
#             # o valor deve ser igual a zero e os demais devem ser calculados
#             if i == 0:
#                 integral.write(str(0) + '\n')
#             else:
#                 integral.write(str(metodoDosRetangulos(i)) + '\n')
# else:
#     print('Valor inserido inválido!')
