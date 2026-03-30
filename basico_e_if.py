print('Hello World !')
print('2*9 = ')
print(2*9)

print('2'+ '3')
print('olá, ' + 'mundo') #ou print('olá,','mundo ')
print(2 + 3 * 3)
print(4**2 / 3) 
print(( 9 ** 2 + 2 ) * 6 - 1)

a = 1 # a recebe 1
b = 3
resposta = a == b
print(resposta)

resposta_2 = a != b
print (resposta_2)

#tamanho( quantidade de caracteres)
s8 = 'logica de programacao e algoritmos'
tamanho = len(s8)
print(tamanho)

nome = 'filipe'
boll = len(nome) <= 15 #len diz o número de itens em um objeto
print(nome)

'''
Docstring(não é comentário) é lido
'''
print(45, 55, 45, sep='-', end='...') 
print(12, 65, end='**')
print('joão \' otávio') 
print(r'João \' otávio \'') 
print(" 'joão' e 'otávio' ")

#IFs
idade = 25
salario = 4000
if idade >= 18:
    print("Maior de idade")
if salario > 3000:
    print("Ganha bem") #sai mesmo se o outro sair também

#If + elif + else, apenas uma condição deve ser executada.
num1 = int(input('Digite um número inteiro: '))
num2 = int(input('Digite outro número inteiro: '))
if num1 > num2:
    print('O primeiro número é maior que o segundo')
elif(num1 == num2): #os parentêses são opcionais
    print('Os dois números são iguais') 
else:
    print('o segundo número é maior que o primeiro')

#Ifs aninhados(condição dentro de outra condição)
idade = 20
tem_carteira = True
if idade >= 18:
    if tem_carteira:
        print("Pode dirigir")
    else:
        print("Precisa ter carteira")
else:
    print("Menor de idade")

# NOT
x = True
y = False
print(not x) #not True = False
print(not y)

# AND
x = True
y = False
print(x and y)

if(min(12, 45, 32) < 30): #MMC
    print('É verdadeiro')

#Operadores lógicos
idadeAna = 32
idadeBeatriz = 29
print(idadeAna >= idadeBeatriz)
print(idadeAna < idadeBeatriz)
print( not(idadeAna<idadeBeatriz))
p = True
print(p)
print(not p)
M=float(input('Média obtida: '))
F=float(input('Total de faltas: '))
if M>=70 and F<=20: 
  print('Aprovado')
else:
  print('Reprovado')
