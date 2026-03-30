# exemplo: um Menu ao longo de um extenso programa.
print('|','__' * 10,'|')
print('|','__' * 10,'|')
print('    MENU    ')
print('|','__' * 10,'|')
print('|','__' * 10,'|')

def realce(): # corpo da função(realce irá armazenar isso)
  print('|','__' * 10,'|')
  print('|','__' * 10,'|')

#Programa principal
realce()
print('     MENU     ')
realce()

def saudacao(nome):   # 'nome' é o parâmetro
    print(f"Olá, {nome}!")
saudacao('Filipe') # Filipe é o argumento

def sub2(x, y):
  res = x - y
  print(res)
sub2(8,9) #a ordem sempre vai importar!

def soma3(x = 0, y = 0, z = 0, imprime=False):
  res = x + y + z
  if imprime:
    print(res)
soma3(1,2,3)
soma3(1,2,3, True) #nesse caso o print irá aparecer na tela
#soma3(1,2, True), aqui está errado pois estamos fazendo z = True
soma3(1,2, imprime=True) # colocando o imprime para dizer que não é o z.

#RETORNO DE VALORES EM FUNÇÕES
def soma3(x, y, z): # obrigatório passar 3 argumentos.
  res = x + y + z
  print(res) # não podemos reutilizar o resultado
def soma3(x=0, y=0, z=0): # parâmetros com valores padrão
  res = x + y + z
  return res # é retornado, não só exibido. guardar em variáveis

#Programa principal
retornado = soma3(2,2,0)
print(retornado)

#forma alternativa simplificada
print(soma3(2,2))