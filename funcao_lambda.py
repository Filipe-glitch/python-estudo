res = lambda x: x * x
print(res(3))
# Função que recebe dois valores, o a soma 5 e multiplica pelo b
calc = lambda a, b: (a + 5) * b
print(calc(5, 10))

# EXEMPLO:
def minha_funcao(x, y):
  """
  Esta função recebe dois números e retorna a soma deles.

  Parâmetros:
  x (int/float) : primeiro número
  y (int/float) : segundo número

  Retorna:
  int/float : soma de x e y
  """
  return x + y


# Métodos com strings
s1 = 'Lógica de Programação e Algoritmos'
s1.endswith('Algoritmos') #Verifica se caracteres existem no final da string
s1.startswith('Lógica')  # Verifica se caracteres existem no início da string
s1.lower().endswith('algoritmos') #Converte string para minúscula
print(s1.upper()) # converte string para maiúscula
s1.count('a') # contar a ocorrência de um caractere (ou vários) dentro de uma string
s1.split(' ') # a string foi quebrada sempre onde apareceu um espaço
s1.replace('Lógica','lógica',1 ) #substituição de string + quantas vezes substituir

from math import sqrt 
print(sqrt(9))

# Desempacotamento de parâmetros em funções
def soma(*num): # o * essa variável será uma tupla de tamanho qualquer
  acumulador = 0
  print('Tupla: {}'.format(num))
  for i in num:
    acumulador += i
  return acumulador
#Programa principal
print(f'Resultado: {soma(1,2)}\n')
print(f'Resultado: {soma(1,2,3,4,5,6,7,8,9)}\n')