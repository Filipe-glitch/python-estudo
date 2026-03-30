# Soma de 5 valores inteiros.
soma = 0 # acumula os valores digitados pelo usuário.
cont = 1 # controla quantas vezes o laço while vai rodar.
while (cont <= 5): #loop vai rodar enquanto cont for menor ou igual a 5.
  x = float(input(f'Digite a {cont}ª nota:'))
  soma = soma + x # Atualiza o valor da soma, adicionando o número digitado.
  cont = cont + 1 # Aumenta o contador em 1. While vai rodar apenas 5 vezes.
print(f'Somatório: {soma}') #Fim do laço, o programa mostra o resultado final.

# média final dos valores digitados
soma = 0
cont = 1
while (cont <= 5):
  y = float(input(f'Digite a {cont}ª nota:'))
  soma = soma + y
  cont = cont + 1
media = soma / 5
print(f'Média final: {media}')

# média dos valores digitados
soma = 0
qtd_num = 0
x = 0
while True:
  t = int(input('Digite um valor inteiro: '))
  if t < 0:
    continue
  if not t:
    break
  soma += t
  qtd_num += 1
media = soma / qtd_num
print(f'A média dos valores digitados é: {media}')

# algoritmo que calcule a média dos números pares de 1 até 100
soma = 0
qtd = 0
for i in range(1,101):
  if (i % 2 == 0):
    soma += i
    qtd += 1
media = soma / qtd
print(f'A média dos pares de 0 até 100 é: {media}')

# A tabuada de todos os números de 1 até 10.
tabuada = 1  #USANDO 2WHILE
while tabuada <= 10:
  print(f'TABUADA DO {tabuada}:')
  i = 1
  while i <= 10:
    print(f'{tabuada} x {i} = {tabuada * i}')
    i += 1
  tabuada += 1
#ou , # USANDO 2for
for tabuada in range(1, 11, 1):
  print(f'TABUADA DO {tabuada}:')
  for i in range(1, 11, 1):
    print(f'{tabuada} x {i} = {tabuada * i}')

# ou , USANDO while + for
tabuada = 1
while tabuada <= 10:
  print(f'TABUADA DO {tabuada}:')
  for i in range(1, 11, 1):
    print(f'{tabuada} x {i} = {tabuada * i}')
  tabuada += 1