mochila = ('Machado', 'Camisa', 'Bacon', 'Abacate')
print(mochila)
print(mochila[0]) #print do Elemento 1 - Índice 0
print(mochila[2]) #print do Elemento 3 - Índice 2
print(mochila[0:2]) #print dos Elementos 1 e 2 - Índice 0 e 1
print(mochila[2:]) # print dos elementos a partir do índice 2
print(mochila[-1]) #print do último
#mochila[2] = 'Ovos' , aqui dará erro pois é imutável
for item in mochila:
  print('Na minha mochila tem: {}'.format(item)) 

tam = len(mochila)
for i in range (0, tam, 1):
  print('Na minha mochila tem: {}'.format(mochila[i]))

upgrade = ('Queijo', 'Canivete')
mochila_grande = mochila + upgrade # pode colocar mais strings nessa tupla
mochila_grande_invertida = upgrade + mochila
print(mochila_grande)
print(mochila_grande_invertida) #a ordem irá importar

#LISTAS
mochila = ['Machado', 'Camisa', 'Bacon', 'Abacate']
print('Lista: ', mochila)
mochila[2] = 'Laranja'
print('Lista: ', mochila)
mochila.append('Ovos')  #adiciona no final da lista
mochila.insert(1,'Canivete') #insere no índice informado
del mochila[1] #deleta do índice informado
mochila.remove('Ovos') #deleta o dado informado
# pode acessar os índices individuais da string dentro de um único índice de uma lista.
print(mochila[0][0])
print(mochila[2][1])

#Cópia de listas:
lista_original = [5, 7, 9, 11]
lista_referenciada = lista_original  # mesma referência
print(lista_original)
print(lista_referenciada) # os dois serão o mesmo.
lista_referenciada[0] = 2 # nas duas listas serão alteradas, pois uma é um clone da outra.
#lista_referenciada = lista_original[:] # dois pontos fazem que a alteração seja na lista desejada.
print(lista_original)
print(lista_referenciada)

mochila = ['Machado', 'Camisa', 'Bacon', 'Abacate']
for item in mochila:
  for letra in item:
    print(letra, end='') #Para fazer varredura dupla de índices, coloca dois laços de repetição aninhados.
  print()

mochila = ['Machado', 'Camisa', 'Bacon', 'Abacate']
for i in range(0,len(mochila),1):
  for j in range(0,len(mochila[i]),1):
    print(mochila[i][j], end='')
  print()

# Dicionários
game = {'nome':'Super Mario',
'desenvolvedora':'Nintendo',
'ano':1990}
print(game)
print(game['nome']) # aqui irá aparecer o Super Mário.
print(game.values())
#or
for values in game.values(): #Super Mario, Nintendo, Ano
  print(values)
for keys in game.keys(): #nome, desenvolvedora,ano
  print(keys)
print(game.items()) #dict_items([(‘nome’, ‘Super Mario’), (‘desenvolvedora’, ‘Nintendo’)...