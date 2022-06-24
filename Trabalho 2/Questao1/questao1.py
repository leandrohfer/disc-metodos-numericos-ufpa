"""
    Trabalho 2 de Métodos Numéricos

    @autor Leandro_Henrique

===========================================================================
Questão 1) Resolver o sistema linear abaixo usando o método de Gauss-Seidel.

     9x - 2y + 3z  + 2w  = 54,5
     2x + 8y - 2z  + 3w  = -14
    -3x + 2y + 11z - 4w  = 12,5
    -2x + 3y + 2z  + 10w = -21

Chute Inicial: A1 = B1 = C1 = D1 = 0
Quantidade desejadas de iterações do método: 7 iterações
===========================================================================
"""

# Definindo os valores dos chutes iniciais
a1 = b1 = c1 = d1 = 0

for i in range(1, 8):

    # Cálculo do valor de X
    xN = (54.5 + 2*b1 - 3*c1 - 2*d1) / 9

    # Cálculo do valor de Y com o valor já calculado de X
    yN = (-14 - 2*xN + 2*c1 - 3*d1)/8

    # Cálculo do valor de Z com o valor já calculado de X e Y
    zN = (12.5 + 3*xN - 2*yN + 4*d1)/11

    # Cálculo do valor de K com o valor já calculado de X, Y e Z
    wN = (-21 + 2*xN - 3*yN - 2*zN)/10

    b1 = yN
    c1 = zN
    d1 = wN

    print('Iteração '+str(i)+': {X1 = '+str(xN)+', X2 = '+str(yN)+', X3 = '+str(zN)+', X4 = '+str(wN)+' }')