import os 

contatos = []

# Menu de Opeções 
def menu_de_opções():
    print(''' ====Agenda de Contatos====
| [ 1 ] - Adicionar contato |
| [ 2 ] - Ver contatos      |
| [ 3 ] - Editar contatos   |
| [ 4 ] - Remover contatos  |
| [ 5 ] - Sair              |''')

while True:

    menu_de_opções()
    escolhar_de_opções = int(input('Escolha uma das opção: '))

    # Adiciona contato
    if escolhar_de_opções == 1:
        os.system('cls')
        nome = str(input('Digite o nome do contato: '))
        telefone = int(input('Digite o número do contato: '))
        email = str(input('Digite o e-mail do contato: '))
        print('Cantato adicionado com sucesso!')
        contatos.append({
            'Nome': nome,
            'Telefone': telefone,
            'E-mail': email
        })

    elif escolhar_de_opções == 2:
        if not contatos:
            print('Nenhum contato adicionado.')
        else:
            contatos = []

            for dados in contatos:
                print(f'Nome do contato: {dados['Nome']}')
                print(f'Telefone do contato: {dados['Telefone']}')
                print(f'E-mail do contato: {dados['E-mail']}')