#ERROS
try:
    x = int(input("Digite um número: "))
    y = 10 / x
    print("Resultado:", y)
except ValueError:
    print("Erro: você não digitou um número válido.")
except ZeroDivisionError:
    print("Erro: não é possível dividir por zero.")
finally:
    print("Fim do programa.")

#ESCOPOS
def omelete():
  ovos = 12  # 'variável local de omelete' , o segundo print
  print('Ovos = ', ovos)
def bacon():
  ovos = 6  # 'variável local de bacon' o primeiro print
  print('Ovos = ', ovos)
  omelete()
  print('Ovos = ', ovos) # o terceiro print , ele está fora do omelete
ovos = 2  # 'variável global'/ último print
bacon()
print('Ovos = ', ovos)

def omeleti():
  global ovo # função mexe na variável global
  ovo = 6 # o ovo global muda de 4 para 6.
  bacon()
def baco(): # ovo = 12 cria uma variável local de baco
  ovo = 12
  pimente()
def pimente(): # não tem uma variável ovos local nem global
  print(ovo)
# Programa principal
ovo = 4
omeleti() # O global continua 6 (porque omeleti mudou o global).
print(ovo) # irá sair o 6 e 6

ovi = 12
omelete()