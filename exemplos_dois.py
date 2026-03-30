# cadastro de notas + soma das notas
print('--------- Cadastro de notas ---------')
rg=input('RG (s/n): ')
cpf=input('CPF (s/n): ')
if rg=='s' or cpf=='s':
  print('Entrada liberada.')
else:
  print('Entrada não autorizada.')

AP1 = int(input('Digite a nota da atividade prática 1:'))
AP2 = int(input('Digite a nota da atividade prática 2:'))
PO = int(input('Digite a nota da prova objetiva:'))
nota = AP1 * 0.2 + AP2 * 0.3 + PO * 0.5
print('nota da disciplina:', nota)
if nota < 30:
  print('REPROVADO')
elif nota >= 30 and nota < 70:
  print('EXAME')
elif nota >= 70 and nota <= 100:
  print('Aprovado')

#Delivery de marmitas
frase = ('-' * 5 + ' Bem-vindo ao delivery de marmitas de Filipe Rocha ' + '-' * 5)
frase2 = ('-' * 25 + ' Cardápio ' + '-' * 26 )
print(frase)
print(frase2)
print('-' * 61)
print('-' * 3 + ' | ' + 'Tamanho' + ' | ' + 'Bifé acebolado(BA)' + ' | ' + 'Filé de Frango(FF)' + ' | ' + '-' * 3 )
print('-' * 3 + ' | ' + '   P   ' + ' | ' + '     R$ 16,00     ' + ' | ' + '     R$ 15,00     ' + ' | ' + '-' * 3 )
print('-' * 3 + ' | ' + '   M   ' + ' | ' + '     R$ 18,00     ' + ' | ' + '     R$ 17,00     ' + ' | ' + '-' * 3 )
print('-' * 3 + ' | ' + '   G   ' + ' | ' + '     R$ 22,00     ' + ' | ' + '     R$ 21,00     ' + ' | ' + '-' * 3 )
soma = 0
valor = 0 #coloquei esse valor igual a 0 para evitar o aviso do pycharm dizendo "valor can be undefined".
while True:
    sabor = input('Digite o sabor desejado:').upper()
    if sabor != 'BA' and sabor != 'FF':
        print('Sabor inválido. Tente novamente')
        continue
    tamanho = input('Digite o tamanho do pedido:').upper()
    if tamanho != 'P' and tamanho != 'G' and tamanho != 'M':
        print('Tamanho inválido. Tente novamente')
        continue
    if sabor == 'BA':
        if tamanho == 'P':
            valor = 16.00
        elif tamanho == 'M':
            valor = 18.00
        else:
            valor = 22.00
    elif sabor == 'FF':
        if tamanho == 'P':
            valor = 15.00
        elif tamanho == 'M':
            valor = 17.00
        else:
            valor = 21.00

    soma += valor
    print(f'Você pediu um {sabor} no tamanho {tamanho}: R${valor:.2f} ')

    outro = input('Deseja pedir mais alguma coisa?').upper()
    if outro == 'S':
        continue
    elif outro == 'N':
        break
    else:
        print('Opção inválida. Encerrando o programa.')
        break
print(f'O valor total a ser pago: R${soma:.2f}')

