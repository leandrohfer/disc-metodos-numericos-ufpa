"""
    Trabalho 2 de Métodos Numéricos

    @autor Leandro_Henrique

===========================================================================
Questão 3) Apresentar os dados de salinidade da água do oceano nas 
profundidades 250m, 750 e 1800m. Dados:

Profundidade em Metros = [0, 100, 200, 300, 400, 500, 600, 700, 800, 900, 
1100, 1400, 2000, 3000]

Salinidade (ppt) = [35.5, 35.35, 35.06, 34.65, 34.48, 34.39, 34.34, 34.32, 
34.33, 34.36, 34.45, 34.58, 34.73, 34.79]


OBS.: Encontre o polinômio interpolador de Lagrange e utilize-o.
===========================================================================
"""

# Definição de função que corresponde ao Método de Lagrange
def metodoLagrange(vetorProf, vetorSal, vetorProfundidadeDesejada):
# X = [0, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1100, 1400, 2000, 3000]
# Y = [35.5, 35.35, 35.06, 34.65, 34.48, 34.39, 34.34, 34.32, 34.33, 34.36, 34.45, 34.58, 34.73, 34.79]
    
  vetorV0 = []
  vetorV1 = []
  vetorV2 = []
  
#   x = [250, 750, 1800]
  for i in range(0, len(vetorProf)):

    V0 = V1 = V2 = 1

    for j in range(0, len(vetorProf)):
    
      # Validação para não alterar o primeiro valor da série
      if i != j:

        # Multiplicação dos valores e atribuindo os mesmos às variáveis criadas
        V0 = V0 * (vetorProfundidadeDesejada[0] - vetorProf[j]) / (vetorProf[i] - vetorProf[j])
        V1 = V1 * (vetorProfundidadeDesejada[1] - vetorProf[j]) / (vetorProf[i] - vetorProf[j])
        V2 = V2 * (vetorProfundidadeDesejada[2] - vetorProf[j]) / (vetorProf[i] - vetorProf[j])

    # Inserção dos valores ao final do array criado para cada profundidade
    vetorV0.append(V0)
    vetorV1.append(V1)
    vetorV2.append(V2)

  Profundidade0 = Profundidade1 = Profundidade2 = 0

  for k in range(0, len(vetorProf)):

    # Soma dos valores e atribuição dos mesmos ao valor de cada profundidade
    Profundidade0 = Profundidade0 + vetorSal[k]*vetorV0[k]
    Profundidade1 = Profundidade1 + vetorSal[k]*vetorV1[k]
    Profundidade2 = Profundidade2 + vetorSal[k]*vetorV2[k]

  # Exibição dos dados de forma organizada
  print('\n')
  print('============Dados fornecidos pela questão============')
  print('Profundidade (metros) ->',vetorProf)
  print('Salinidade (ppt) ->',vetorSal)
  print('--------------------------------------------------------------------------')
  print('\n')
  print('============Dados obtidos após os cálculos============')
  print("Profundidade 250m ->", Profundidade0, "ppt")
  print("Profundidade 750m ->", Profundidade1, "ppt")
  print("Profundidade 1800m ->", Profundidade2, "ppt")
  print('--------------------------------------------------------------------------')

# Definição de valores com os dados da questão
Profundidade = [0, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1100, 1400, 2000, 3000]
Salinidade = [35.5, 35.35, 35.06, 34.65, 34.48, 34.39, 34.34, 34.32, 34.33, 34.36, 34.45, 34.58, 34.73, 34.79]

ProfundidadesDesejadas = [250, 750, 1800]

# Chamada a função que foi criada
metodoLagrange(Profundidade, Salinidade, ProfundidadesDesejadas)

