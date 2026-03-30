import pandas as pd  # usada para trabalhar com tabelas e dados.
x={'Pesos':[48.8, 48.9, 49.0, 49.1, 49.2, 49.3, 49.5, 49.7,
49.7, 49.7, 49.8, 50.0, 50.1, 50.1, 50.2, 50.2, 50.4, 50.6,
50.8, 50.9]} 
p=pd.DataFrame(x) 
media=p['Pesos'].mean()
moda=p['Pesos'].mode()  
mediana=p['Pesos'].median() 
print(f'Média: {media}')
print(f'Moda: {moda}')
print(f'Mediana: {mediana}')

#DESVIO PADRÃO e Variância por σ2
x={'Peso':[48.8, 48.9, 49.0, 49.1, 49.2, 49.3, 49.5, 49.7,
49.7, 49.7, 49.8, 50.0, 50.1, 50.1, 50.2, 50.2, 50.4, 50.6,
50.8, 50.9]}
p=pd.DataFrame(x)
desviopadrao=p['Peso'].std() #comando para ter o desvio padrão
print(f'Desvio padrão: {desviopadrao}')
variancia = p['Peso'].var()
print(f'Variância: {variancia}')

#PROBABILIDADE:
# Projetor com 5000 horas e desvio padrão de 300 horas. 
# probabilidade de durar entre 5000 e 5500 horas.
import scipy.stats 
media= 5000  
desvio_padrao= 300  
X= 5500 

# valores de X acima da média
p=scipy.stats.norm(media,desvio_padrao).cdf(X)-0.5
print(p)

# valores de X abaixo da média
p=0.5-scipy.stats.norm(media,desvio_padrao).cdf(X)

#ESTATISTICA: 
# EXEMPLO: 20000 pessoas e margem de erro de 2%?
from math import ceil 
N = 20000 
e = 0.02
n = ceil(N / (1 + N * e**2))
print(f'Tamanho da amostra: {n}')

from scipy.interpolate import *
x=[]
y=[]
p=lagrange(x, y)
print(p)

#POLINÔMIOS
# Interpola os pontos A(4, 2), B(7, -1), C(10, 12) e D(11,15)
from scipy.interpolate import *
x=[4, 7, 10, 11]
y=[2, -1, 12, 15]
p=lagrange(x, y)
print(p) # -0.1746 x3 + 4.556 x2 - 34.87 x + 79.78

# Partículas estão se alterando com o passar do tempo.
# Dados: 1 ano - 80, 2 ano - 95, 3 ano - 110, 4 ano - 122
from scipy.interpolate import *
x=[1, 2, 3, 4] # polinômio que interpola esses dados
y=[80, 95, 110, 122]
p=lagrange(x, y)
print(p) # p(x) = -0,5x3 + 3x2 + 9,5x + 68.

#Aritmetica modular:
n = (3 + 4) % 5 # % é o resto da divisão 7 / 5