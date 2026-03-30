# MATRIZES
#
#    ( 400 10 )
#F1 =( 480 12 )
#    ( 600 15 )
#              ( 31 11 )
#         F2 = ( 37 11 )
#              ( 48 11 )

# indústria de cadeiras possui três modelos denominados de A, B e C, e possui duas fábricas chamadas de F1 e F2.
# fábrica F1, são produzidas as peças e, na fábrica F2, é feita a montagem das cadeiras.
# produção: A=400, B=480 e C=600 ; transporte: A=10, B=12, C=15
# Montagem: A=31, B=37 e C=48 ; transporte: A=11, B=11, C=11
# custos totais de produção e de transporte referentes a cada modelo de cadeira
import numpy as np
F1=np.array([[400, 10],[480, 12],[600, 15]])
F2=np.array([[31, 11],[37, 11],[48, 11]])
CustoTotal=F1+F2
print(CustoTotal)

#HOUVE AUMENTO DE 10% na fabricação das peças e nos custos de transporte.
F1=np.array([[400, 10],[480, 12],[600, 15]])
F1=1.1*F1
print(F1)

#MULTIPLICAÇÃO DE MATRIZES
A=np.array([[3, 1, 3],[6, 5, 5]])
B=np.array([[100, 50],[50, 100],[50, 50]])
C=np.matmul(A, B) # multiplicador de matrizes
print(C)

#FUNÇÕES
# Custo unitário da produção é 28 e mensalmente x unidades são produzidas
# custo mensal de produção C, C(x) = 28x
import matplotlib.pyplot as plt
x=np.linspace(0, 10, 100) # cria 100 números igualmente espaçados entre 0 e 10.
y=28*x
plt.plot(x,y)
plt.show()

#se fosse produzida 2334. x = 2344, y = 28 * x , print(y)

#FUNÇÃO QUADRATICA
# lucro mensal de estacionamento com preço cobrado por hora é L(x)=-340x2+5700x-9500
# x = preço por hora, L = lucro mensal. Contrua o gráfico
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, 16, 100)
y = -340 * x ** 2 + 5700 * x - 9500
plt.plot(x, y)
plt.show()
 # Preço ótimo: R$ 8,38  conceito de Xv = -b/2a
 # Lucro máximo: R$ 14.389,71 conceito de Yv= -delta/(4 * a)