# Recebe três valores como parâmetro e coloque em ordem crescente e imprima-os.
def maior3(v1=0, v2=0, v3=0):
  if (v1 and v2 and v3):
     if ((v1 > v2) and (v1 > v3)):
        if (v2 > v3):
          print(f'Ordem crescente: {v3}, {v2}, {v1}')
        else:
          print(f'Ordem crescente: {v2}, {v3}, {v1}')
     elif ((v2 > v1) and (v2 > v3)):
        if (v1 > v3):
          print(f'Ordem crescente: {v3}, {v1}, {v2}')
        else:
          print(f'Ordem crescente: {v1}, {v3}, {v2}')
     elif ((v3 > v1) and (v3 > v2)):
        if (v1 > v2):
          print(f'Ordem crescente: {v2}, {v1}, {v3}')
        else:
          print(f'Ordem crescente: {v1}, {v2}, {v3}')
# Programa Principal
x = int(input('Digite o valor 1: '))
y = int(input('Digite o valor 2: '))
z = int(input('Digite o valor 3: '))
maior3(x, y, z)

# Lê um nome e solicita um índice, mais print do caractere no respectivo índice.
i = 0
while True:
    try:
        nome = input('Por favor digite o seu nome: ')
        ind = int(input('Digite um índice do seu nome digitado: '))
        print(nome[ind])
        break
    except ValueError:
        print('Oops! Nome inválido. Tente novamente...')
    except IndexError:
        print('Oops! índice inválido. Tente novamente...')
    finally:
        print(f'Tentativa {i}')
        i += 1

# validação recebe como parâmetro um inteiro e o intervalo em que o valor digitado deve estar.

def valida_int(pergunta, min, max):
  x = int(input(pergunta))
  while ((x < min) or (x > max)):
    x = int(input(pergunta))
  return x
#Programa principal
x = valida_int('Digite um valor inteiro: ', 0, 100)
print(f'Você digitou {x}. Encerrando o programa...')