#WHILE(enquanto)
x = 1
while (x <= 5):
  print(x)
  x = x + 1 


while True:
  nome = input('Qual o seu nome?')
  if (nome != 'Filipe' or 'filipe'):
    continue # volta para inicio do laço
  senha = input('Qual a sua senha?')
  if (senha == '1234abM'):
    break # encerra o laço
print('Acesso concedido.')


nome2 = ''
while not nome2:
  # encerra o laço quando nome não estiver vazio
  nome2 = input('Digite seu nome:')
valor = int(input('Digite um número qualquer:'))
if valor: #Equivalente if valor != 0:
  print('Você digitou um valor diferente de zero.')
else:
  print('Você digitou zero.')

#FOR
frase = "Lógica de Programação e Algoritmos"
for i in range(0, len(frase), 1):
  print(frase[i])

frase2 = "Lógica de Programação e Algoritmos"
for i in range(0, len(frase), 1):
  print(frase2[i], end="")

# A contagem vai de 10 a 0 contando de -2 em -2
for i in range(10,0,-2):
  print(i)

u = 1
for _ in range(3):
    for _ in range(3):
        print(i, end=' ')
        i+=1
    print() #matriz