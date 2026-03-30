frase = 'olá, mundo!'
print (frase)
print (frase[0]) #começa sempre pelo 0
print (frase[3]) #entre colchetes temos a posição que queremos

#Concatenação
s1 = 'A' + '-' * 10 + 'B' #s1 = 'A' + '----------' + 'B'
print(s1)
s2 = 'Lógica de programação'
s2 = s2 + ' e algoritmos'
print(s2)

nota_2 = 8.9
s3 = 'você tirou %.2f na disciplina de algoritmos' % nota_2
print(s3)

nota_3 = 7.6
disciplina = 'algoritmos'
s4 = 'você tirou %.4f na disciplina de %s ' % (nota_3, disciplina)
print(s4) # aqui são várias variáveis

#Composição moderna
nota_4 = 4.6
disciplina_2 = 'lógica'
s5 = 'você tirou {} na disciplina de {}' .format(nota_4,disciplina_2)
print(s5)

#Composição por f-string (prefira essa)
nota_5 = 7.4
disciplina_3 = 'programação'
s6 = f'você tirou {nota_5} na disciplina de {disciplina_3}'
print(s6)

#fatiamento de strings
s7 = 'Estudos com Python'
print(s7[0:7]) # termina com um a mais sempre # ou print(s7[:7])
print(s7[8:11])
print(s7[12:18]) # ou print(s7[12:])

# Variável string com quebra de linha (\n), tabulação (\t) e multiplicador de strings
mensagem = "Linguagens de programação:\n" + "\tPython" + " ----- " + "C" + " ----- " + "Java" + " ----- " + "PHP\n"
mensagem += "-" * 40
print(mensagem)

food = 'lasanha'
ano = 2004
divisao = 2004/23
#mensagem_2 = 'Minha comida favorita é %s e um ano é %d e essa divisão do ano por um númeroé %d' %(food, ano , divisao)
#mensagem_2='Minha comida favorita é {} eumano é {} e essa divisão doano porum númeroé é {}'.format(food, ano, divisao)
mensagem_2 = f'Minha comida favorita é {food} e um ano é {ano} e essa divisão do ano por um número é {divisao}'
print(mensagem_2)

#conversão para não ser string
nota_6 = float(input('Qual é a sua nota na disciplina?'))
print(f'você tirou {nota_6}')

nome_2 = input('qual é o seu nome?')
idade = input('quantos anos você tem?')
print(f'olá {nome_2}, com {idade} anos de idade, seja bem vindo ao curso de python')