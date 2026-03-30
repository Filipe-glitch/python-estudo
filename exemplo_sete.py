print('Bem-vindo a Fábrica de Camisetas de Filipe Rocha\n')
def escolha_modelo():
    while True:
       print('MCS - Manga Curta Simples')
       print('MLS - Manga Longa Simples')
       print('MCE - Manga Curta com Estampa')
       print('MLE - Manga Longa com Estampa')
       modelo = input('\nEscolha o modelo de camiseta que deseja: ').upper()
       if modelo == 'MCS':
         return 1.80
       elif modelo == 'MLS':
         return 2.10
       elif modelo == 'MCE':
         return 2.90
       elif modelo == 'MLE':
         return 3.20
       else:
         print('Modelo inválido, digite o modelo novamente: ')

def num_camisetas():
    while True:
       try:
         quantidade = int(input('Digite a quantidade de camisetas desse modelo que deseja:'))
         if quantidade > 20000:
             print('Não aceitamos tantas camisetas de uma vez')
             continue
         if quantidade < 20 :
             desconto = 0.0
         elif 20 <= quantidade < 200:
             desconto = 0.05
         elif 200 <= quantidade < 2000:
             desconto = 0.07
         else:
             desconto = 0.12

         return quantidade, desconto
       except ValueError:
         print('Valor inválido! Digite o número de camisetas: ')

def frete():
    while True:
        print('Escolha o tipo de frete:\n')
        print('1 - Transportadora - R$ 100,00')
        print('2 - Sedex - R$200,00')
        print('0 - Retirar o pédido na Fábrica - R$ 0,00')

        entrega = input('Escolha a opção de frete: ')

        if entrega == '1':
            return 100.00
        elif entrega == '2':
            return 200.00
        elif entrega == '0':
            return 0.00
        else:
            print('Por favor, digite o número referente ao frete almejado:')

preco = escolha_modelo()
quantidade, desconto = num_camisetas()
valor_frete = frete()
total = (preco * quantidade) * (1 - desconto) + valor_frete

print(f'Total = R${total:.2f}')