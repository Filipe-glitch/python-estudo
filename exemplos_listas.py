# cadastro de lista de compras que deverão ser registradas.
item = []
mercado = []
for i in range(3):
  item.append(input('Digite o nome do item:'))
  item.append(int(input('Digite a quantidade:')))
  item.append(float(input('Digite o valor:')))
  mercado.append(item[:])
  item.clear()
print(mercado)

# Cadastro de lista de jogos
game = {}
games = []
# Lista contendo, em cada índice, um dicionário
for i in range(3):
  game['nome'] = input('Qual o nome do jogo?')
  game['videogame'] = input('Para qual video game ele foi lançado?')
  game['ano'] = input('Qual o ano de lançamento?')
  games.append(game.copy())
print('-' * 20)
for jogos in games:
  for chave, valor in jogos.items(): \
    print(f'O campo {chave} tem o valor {valor}.')

# Criação da inserção dos dados no dicionário com listas via teclado

games = {'nome':[],'videogame':[],'ano':[]}
for i in range(3):
  nome = input('Qual o nome do jogo?')
  videogame = input('Para qual video-game ele foi lançado?')
  ano = input('Qual o ano de lançamento?')
  games['nome'].append(nome)
  games['videogame'].append(videogame)
  games['ano'].append(ano)
print('-' * 20)
print(games)