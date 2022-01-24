# criando cadastro em python
import time

login_lst = []
senha_lst = []

def busca_cadastro():
    user = input('Digite seu usuário: ')
    for cadastro in range(0,len(login_lst)):
        if user == login_lst[cadastro]:
            continue
        else:
            print('Usuário incorreto.')
            break
            
    senha = input('Digite sua senha: ')
    for senhas in range(0,len(senha_lst)):
        if senha == senha_lst[senhas]:
            print('Logado com sucesso!')

        else:
            print('Senha incorreta.')
            break

while True:
    login = input('Olá! Deseja criar um novo login (\'C\') ou usar um existente (\'L\') (Se deseja cancelar, pressione \'N\')? ').upper()

    if login == "C":
        user = input('Digite um novo usuário: ')
        senha = input('Digite uma nova senha: ')
        login_lst.append(user)
        senha_lst.append(senha)
        print('Processando...')
        time.sleep(1)
        print('...')
        time.sleep(1)
        print('Usuário', user, ' e senha', senha, ' foram criados!')
        continuar = input('Deseja entrar em sua conta (S/N)? ').upper()
        if continuar == 'S':
            busca_cadastro()

        elif continuar == 'N':
            print('Certo. Parando programa.')
            break
        else:
            print('Caractére inválido.')

    elif login == 'L':
        busca_cadastro()

    elif login == 'N':
        print('Cancelando. Até mais!')
        time.sleep(1)
        break
    else:
        print('Caractére inválido.')
        time.sleep(0.5)
        continue            