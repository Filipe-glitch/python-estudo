print('Bem vindo a empresa de Filipe Rocha')
print('-' * 50)
lista_funcionarios = []
id_global = 45465
def cadastrar_funcionario(id):
  print('-' * 17 + 'MENU DE CADASTRO' + '-' * 17)
  print(f'Id do funcionário: {id}')
  nome = input('Digite o nome do funcionário :')
  setor = input('Digite o setor do funcionário: ')
  salario = float(input('Digite o salário: R$'))
  funcionario = {'id': id,'Nome': nome,'setor': setor,'Salário': salario}
  lista_funcionarios.append(funcionario.copy())
def consultar_funcionarios():
    print('-' * 17 + 'MENU DE CONSULTA' + '-' * 17)
    while True:
        print('1. Consultar todos: ')
        print('2. Consultar por Id: ')
        print('3. Consultar por setor: ')
        print('4. Retornar ao menu')
        opc = input('Qual opção deseja: ')
        if opc == '1':
          for f in lista_funcionarios:
            print(f)
        elif opc == '2':
          id_f = int(input('Digite o Id do funcionário: '))
          for f in lista_funcionarios:
            if f['id'] == id_f:
              print(f)
              break
          else:
              print('Não existe esse funcionário!')
        elif opc == '3':
          setor = input('Digite o setor: ')
          meu_setor = False
          for f in lista_funcionarios:
            if f['setor'] == setor:
              print(f)
              meu_setor = True
          if not meu_setor:
            print('setor não encontrado')
        elif opc == '4':
            return
        else:
            print('Opção inválida, tente novamente')

def remover_funcionario():
    print('-' * 18 + 'MENU DE REMOÇÃO' + '-' * 17)
    while True:
        id_f = int(input('Digite o Id do funcionário a ser removido: '))
        for f in lista_funcionarios:
            if f['id'] == id_f:
                lista_funcionarios.remove(f)
                return
        print('Id inválido, digite novamente o Id: ')


#Estrutura do código principal(Main)
while True:
    print('-' * 18 + 'MENU PRINCIPAL' + '-' * 18)
    print('1 - Cadastrar funcionário')
    print('2 - Consultar funcionário')
    print('3 - Remover funcionário')
    print('4 - Encerrar programa')
    opc = input('Qual opção deseja: ')
    if opc == '1':
        cadastrar_funcionario(id_global)
        id_global += 1

    elif opc == '2':
        consultar_funcionarios()
    elif opc == '3':
        remover_funcionario()
    elif opc == '4':
        print('programa encerrado.')
        break
    else:
        print('Opção inválida, tente novamente.')