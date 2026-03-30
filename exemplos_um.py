# Senha + empréstimo interno empresa
print('Senha BKS')
senha = int(input('digite a senha de acesso do sistema:'))
if senha == 999999 or senha ==705080:
    print('Acesso liberado')
else:
    print('ACESSO RECUSADO')

print('-' * 12 + 'Setor de empréstimo da empresa BKS' + '-' * 12)
senha = int(input('Digite a senha: '))
if senha == 705080:
    print('Entrada liberada')
else:
    print('Senha incorreta')

print('-' * 12 + 'Empréstimo da empresa' + '-' * 12)
rm = int(input('Digite o valor do seu salário:'))
empre = int(input('Digite o valor do empréstimo:'))
if rm >= 8500 and empre <= rm * 0.2:
    print('Empréstimo aceito')
else:
    print('Empréstimo recusado')

# Escolha se quer laranja,banana ou maça e + preços e valor.
print('Escolha o que deseja comprar:')
print('1 - Maça')
print('2 - Laranja')
print('3 - Banana')
produto = int(input('Qual sua escolha?'))
qtd = int(input('Quantas unidades?'))
if (produto == 1):
   pagar = qtd * 2.3
   print(f'Você comprou {qtd} maças. Total a pagar: {pagar}')
elif (produto == 2):
   pagar = qtd * 3.6
   print(f'Você comprou {qtd} laranjas. Total a pagar: {pagar}')
elif (produto == 3):
   pagar = qtd * 1.85
   print(f'Você comprou {qtd} bananas. Total a pagar: {pagar}')
else:
   print('Produto inexistente!')

# Pedido loja de roupa
print('Bem-vindo a loja de Filipe Rocha')
valorDoPedido = int(input('Digite o valor do pedido: '))
quantidadeParcelas = int(input('Digite a quantidade de parcelas: '))
if quantidadeParcelas < 4:
    juros = 0
elif quantidadeParcelas >= 4 and quantidadeParcelas < 6:
    juros = 4
elif quantidadeParcelas >= 6 and quantidadeParcelas < 9:
    juros = 8
elif quantidadeParcelas >= 9 and quantidadeParcelas < 13:
    juros = 16
else:
    juros = 32

valorDaParcela = valorDoPedido * (1 + juros / 100) / quantidadeParcelas
valorTotalParcelado = valorDaParcela * quantidadeParcelas
print(f'O valor das parcelas é de: R${valorDaParcela:.2f}')
print(f'O valor total parcelado é de: R${valorTotalParcelado:.2f}')