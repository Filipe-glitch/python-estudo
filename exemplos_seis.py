# Gere um conjunto de números inteiros de -10 a 20 e verifique se -1 está na lista
import numpy as np
C=np.linspace(-10, 20, 31) # -10 o inicio, 20 onde encerra, 31 é a quantidade de elementos
print(C)
print(-1 in C)

#Entrada em residência foram geradas 5 senhas: 452012, 323233, 787910, 528917 e 683524
#crie programa que armazena as senhas e verifica se a senha digitada está correta ou não.
S = [452012, 323233, 787910, 528917, 683524]
u = int(input("Digite a senha: "))
if u in S:
  print('Senha correta. Pode entrar')
else:
  print('senha incorreta. Não pode entrar')

#Vetor v com preços v(1210, 897, 1230, 1495, 799, 890, 1010). 
#Promoção é de desconto de 20%, dê vetor que contenha os descontos
v = np.array([[1210, 897, 1230, 1495, 799, 890, 1010]])
w = 0.8 * v
print(w)

#Dados os vetores z=(3, 4, 8) e w=(10, 12,-1) , tenha o vetor z + w e z - w e z . w
z= np.array([[3, 4, 8]])
w= np.array([[10, 12,-1]])
print(z + w)
print(z - w)
p = np.inner(z,w) # produto escalar NÃO É MULTIPLICAÇÃO
print(p)

#DADA AS MATRIZES A e B, calcule A.B e A+B
#    (3  5  9 )      (12  -6  7)
# A =(4  2  -3)  B = (3   0   2)
#    (1  5  -5)      (-1  10  1)
A=np.array([[3, 5, 9],[4, 2, -3],[1, 5, -5]])
B=np.array([[12, -6, 7],[3, 0, 2],[-1, 10, 1]])
D=A + B
C=np.matmul(A, B)
print(C)
print(D)

#Construa o gráfico da função y=x3-2x2+12x-1 no intervalo [-3, 4].
import matplotlib.pyplot as plt
x=np.linspace(-3, 4, 100)
y= 1*x**3 -2*x**2 + 12*x - 1
plt.plot(-3,4)
plt.show()

#empresa produz carregadores: custos fixos mensais:47.500;
# preço de venda de 12 por unidade, o lucro mensal corresponde a 22.000;
#cada carregador é vendido por 20, o lucro mensal é de 20.450
from scipy.interpolate import *
k = [0, 12, 20]
q = [-47500, 22000, 20450]
m = lagrange(k, q)
print(m)

#Obtenha a soma 7+8 módulo 12
print((7+8) % 12) #3