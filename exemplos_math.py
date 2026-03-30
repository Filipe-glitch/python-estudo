# exercicios matemática na computação
p = True #V(p)=V
q = True #V(q)=V
r = False #V(r)=F
print(p or q) #p + q
print(p or r) #p + r
print(q and r) #q.r
print(not(q and r )) #(q.r)'
print(q or r) #q + r
print(not p) #p'
print(not(p and r )) #(p.q)'

x = bin(12) #os dois primeiros digitos indicam que é um binário
y = bin(12)[2:] #aqui de fato é só o número binário
print(x)
print(y)
z = hex(456) #os dois primeiros digitos indicam que é um hexadecimal
w = hex(12)[2:] #aqui de fato é só o número hexadecimal
u = bin(12332)[2:]
t = hex(15487)[2:]
print(t, u)

#NOTAÇÃO CIENTIFICA
c = 210.12 * 10 ** 1 #exemplo de notação
print(3 **(1/2) **2) # = 2.99999996. sabemos que raiz quadrada de 3 ao quadrado é 2
a = 3242
print('%.10e' % a) #notação cientifica normalizada em python
print('%.4e' % 0.000000054) #5.40000e-06

b = 0.23154
print('%.4e' % b) #2.3241 e-01
print(f'{0.0000054:.4e}') #5.4000e-06 , Usamos f-string

import sys
print(sys.float_info.min) # menor número possível
print(sys.float_info.max) #maior número possível
print(sys.float_info.epsilon) #épsilon da máquina: medir a menor diferença possível entre dois números

y = 2.3421e+02
g = 3.5154e+02
f = y + g
print('%.10e' % f) #5.8575000000e+02

p = 2.3421e+02
h = 3.5154e+04
o = p + h
print('%.10e' % o)

from math import pi
from math import factorial
x_graus=float(input('Informe o valor do ângulo, em graus:'))
termos=int(input('Informe o número de termos do somatório: '))
x_radianos=pi*x_graus/180
seno=0
for n in range(termos):
  seno=seno+(-1)**n*x_radianos**(2*n+1)/factorial(2*n+1)
print(seno)