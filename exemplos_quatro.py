# Projeto de bonificação de uma empresa:
print('Nossa empresa está concedendo uma bonificação para todos os funcionários ')
print('Funcionários com 5 ou mais anos na empresa receberão bonificação de 20%')
print('Funcionários com menos de 5 anos na empresa rebeberão bonificação de 10%')
salario = float(input('Quanto você recebe em nossa empresa? '))
tempo = int(input('Quanto tempo você trabalha em nossa empresa(em anos)? '))
if(tempo < 5):
    print('Seu salário será, a partir de agora:', salario * (1 + 10 / 100), 'reais')
else:
    print('Seu salário será, a partir de agora:', salario * (1 + 20 / 100), 'reais')

# Algoritmo para mostrar se passou de ano, precisa de média maior que sete nas 3 matérias.
media1 = float(input('Digite a nota da 1ª matéria:'))
media2 = float(input('Digite a nota da 2ª matéria:'))
media3 = float(input('Digite a nota da 3ª matéria:'))
if media1 >= 7 and media2 >= 7 and media3 >= 7:
     print('O aluno passou de ano!')
else:
     print('O aluno não passou de ano!')

# Algoritmo para mostrar o preço a se pagar por km rodado sabendo que a diária do carro é 60 e mais 0,15 por km rodado
km = float(input('Quantos quilometros o carro circulou nos dias em que foi alugado pelo senhor? '))
dia = int(input('Quantos dias ele ficou alugado com o senhor? '))
conta = 60 * dia + km * 0.15
print(f'Sua conta será de {conta}')

# Algoritmo que receba 3 valores representando os lados de um triângulo e diga se é isosceles, equilatero ou escaleno
A = int(input('Digite o 1º lado do triângulo:'))
B = int(input('Digite o 2º lado do triângulo:'))
C = int(input('Digite o 3º lado do triângulo:'))
if A > 0 and B > 0 and C > 0:
    if A + B > C and A + C > B and B + C > A:
        # Aqui identificamos que o triângulo é válido
        if A != B and A != C and B != C:
            print('Triângulo escaleno.')
        else:
            if A == B and A == C and B == C:
                print('Triângulo equilátero.')
            else:
                print('Triângulo isósceles.')
    else:
        print('Ao menos um dos valores indicados não servem para formar um triângulo.')
else:
    print('Ao menos um dos valores indicados não servem para formar um triângulo.')

# Algoritmo para soma de dois números
print('Soma de dois números')
numero_um = int(input('digite um número inteiro '))
numero_dois = int(input('digite outro número inteiro '))
print('a soma é ', numero_um + numero_dois)

# Soma de 2 números com f-string
#res = f'O resultado da soma de {x} com {y} é {x + y}.'
#print(res)

# produto de loja + desconto e o valor no pós desconto
preco = float(input('Digite o valor do produto: '))
percentual = float(input('Digite o percentual de desconto(0-100%):  '))
desconto = preco * (percentual / 100)
final = preco - desconto
print(f'O preço do produto é {preco} e o percentual de desconto é {percentual}%')
print(f'O preço final do produto aplicado com desconto é {final}')