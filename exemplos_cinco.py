abs(123450.10-123400)
abs(123450.10-123400)/abs(123450.10)

# erros
x=10
y=0
try:
  x/y
except ZeroDivisionError:
  print('Infelizmente ocorreu um erro. Não é possível realizar uma divisão por zero.')

a = 0.0126551
print('%.6e' % a)
b = 432531
print('%.6e' % b)

c = 5.122132e+03
d = 2.741826e+03
f = d + c
print('%.6e' % f)

r = 1.758911e+02
t = 4.002234e+05
y = t + r
print('%.6e' % y)

p = 3.445161e+03
o = 1.151436e+03

lista=['Ana', 'Beatriz', 'Caio', 'Diego']
print('Diego' in lista) # in significa PERTENCE a lista, caso sim True.

# mercadorias por 22, 12, 54, 89 e 11. compra cada uma por 18, 4, 39, 61 e 8
# Usando o vetor, indique a margem de ganho(venda - compra)
import numpy as np
v=np.array([[22, 12, 54, 89, 11]])
u=np.array([[18, 4, 39, 61, 8]])
m=v-u
print(m)
#np.array cria um vetor ou matriz. criar um array do NumPy
notas=np.array([[90, 85, 70, 100]])
pesos=np.array([[0.2, 0.2, 0.3, 0.3]])
media=np.inner(notas, pesos) #multiplicar um vetor por outro vetor
# 90 * 0.2 + 85 * 0.2 ...
print(media)