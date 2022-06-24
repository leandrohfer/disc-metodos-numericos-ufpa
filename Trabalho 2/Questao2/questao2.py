"""
    Trabalho 2 de Métodos Numéricos

    @autor Leandro_Henrique

===========================================================================
Questão 2) Dado um circuito RC em série, onde temos um resistor de 5 MOhm
conectado em série a um capacitor de capacitância C e uma bateria de força
eletromotriz v, também em série. O experimento inicia pelo fechamento da
chave entre os terminais pelos quais a bateria e o resistor se conectam.

Logo após, a tensão vR entre os terminais do resistor a cada 2 segundos será
medida dentro de um intervalo total de 30 segundos. De acordo com os dados
abaixo:

t (s)     vR (V)
2      |   9,7
4      |   8,1
6      |   6,6
8      |   5,1
10     |   4,4
12     |   3,7
14     |   2,8
16     |   2,4
18     |   2,0
20     |   1,6
22     |   1,4
24     |   1,1
26     |   0,85
28     |   0,69
30     |   0,6


Tensão no resistor é dado pela função: vR = v*e^(-t/(R*C))

Determine o valor da capacitância C pelo ajuste da função exponencial aos 
dados obtidos na medição.
===========================================================================
"""

import math
import numpy as np

# Definição dos dados fornecidos pela questão
vetorTempo = [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30]
vetorTensao = [9.7,8.1,6.6,5.1,4.4,3.7,2.8,2.4,2,1.6,1.4,1.1,0.85,0.69,0.6]
tamanhoVetorTempo = len(vetorTempo)

# Definição dos vetores que serão utilizados
Sxx = []
Sxy = []
Sy = []

# Definição dos Somatórios dos vetores definidos anteriormente
somatorioTempo = somatorioSxx = somatorioSxy = somatorioSy = 0

for indice in range(0, tamanhoVetorTempo):
  # Inserção de valores nos vetores definidos anteriormente
  Sxx.append(vetorTempo[indice] ** 2)
  Sy.append(math.log(vetorTensao[indice], math.e))
  Sxy.append(vetorTempo[indice] * Sy[indice])
  
  # Cálculo dos somatórios
  somatorioTempo += vetorTempo[indice]
  somatorioSxx += Sxx[indice]
  somatorioSxy += Sxy[indice]
  somatorioSy += Sy[indice]

# Realizando o cálculo de a0 e a1
Z= np.array([[tamanhoVetorTempo, somatorioTempo], [somatorioTempo, somatorioSxx]])
W = np.array([somatorioSy, somatorioSxy])

arrayA = np.linalg.solve(Z, W)

# Exibição dos valores de a0 e a1
print('----------------------------------------------')
print('Valor de a0 = ', arrayA[0])
print('Valor de a1 = ', arrayA[1])

# Cálculo da capacitância
R = 5 * 1000000
C = -1 / (R * (arrayA[1]))

print('----------------------------------------------')
print('Valor da capacitância = ', C)

# Cálculo da tensão no resistor a partir da fórmula previamente fornecida
vF = math.exp(arrayA[0]) * math.exp((-(arrayA[1])) * 0)

print('Valor da tensão no resistor = ', vF)
print('----------------------------------------------')