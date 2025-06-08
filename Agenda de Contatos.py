import os 

contatos = []

while True:

# Menu de Opeções 
    print(''' ====Agenda de Contatos====
| [ 1 ] - Adicionar contato |
| [ 2 ] - Ver contatos      |
| [ 3 ] - Procurar contato  |
| [ 4 ] - Editar contatos   |
| [ 5 ] - Remover contatos  |
| [ 6 ] - Sair              |''')
    

    escolhar_de_opções = int(input('Escolha uma das opção: '))

    # Adiciona contato
    if escolhar_de_opções == 1:
        os.system('cls')
        nome = str(input('Digite o nome do contato: ')).strip().upper()
        try:
            telefone = int(input('Digite o número do contato: '))
        except ValueError:
            print('\n"NÃO ADICIONAR LETRAS" Tenta Novamente!\n')
            continue
        email = str(input('Digite o e-mail do contato: '))
        print('\nContato adicionado com sucesso!\n')
        contatos.append({
            'Nome': nome,
            'Telefone': telefone,
            'E-mail': email
        })

    # Ver todos os contatos
    elif escolhar_de_opções == 2:
        if not contatos:
            print('Nenhum contato adicionado.')
        else:
            os.system('cls')
            for dados in contatos:
                print(f'Nome do contato: {dados['Nome']}')
                print(f'Telefone do contato: {dados['Telefone']}')
                print(f'E-mail do contato: {dados['E-mail']}')
                print('==' * 15, '\n')

    # Procurar contato
    elif escolhar_de_opções == 3:
        os.system('cls')
        procurar_contato = str(input('Digita nome do seu contato para procurar: ')).strip().upper()
        achou = False

        for dados in contatos:
            if dados['Nome'] == procurar_contato:
                print(f'\nNome do Contato: {dados['Nome']}')
                print(f'Telefone do Contato: {dados['Telefone']}')
                print(f'E-mail do Contato: {dados['E-mail']}\n')
                achou = True
        
        if not achou:
            print('\nEsse nome não existe na sua agenda de contatos.\n')

    # Editar contato
    elif escolhar_de_opções == 4:
        os.system('cls')
        editar_contato = str(input('Digite o nome do contato para edita-lo da agenda: ')).strip().upper()
        achou = False

        for dados in contatos:
            if dados['Nome'] == editar_contato:
                novo_nome = str(input('\nDigite o nome do contato: ')).strip().upper()
                novo_telefone = int(input('Digite o número do contato: '))
                novo_email = str(input('Digite o e-mail do contato: '))

                # Atualiza os dados
                dados['Nome'] = novo_nome
                dados['Telefone'] = novo_telefone
                dados['E-mail'] = novo_email

                achou = True
                print('\nContato editado com sucesso!\n')
        if not achou:
            print('\nEsse nome não foi encontrado na sua agenda de contatos.\n')

    # Remover contato    
    elif escolhar_de_opções == 5:
        os.system('cls')
        remover_contato = str(input('Digite o nome do contato para remove-lo da agenda: ')).strip().upper()
        achou = False

        for dados in contatos:
            if dados['Nome'] == remover_contato:
                contatos.remove(dados)
                achou = True
                print('\nContato removido com sucesso!\n')
            else:
                print('\nEsse nome não existe na sua agenda de contato.\n')

    # Sair do programa
    elif escolhar_de_opções == 6:
        os.system('cls')
        continuar = str(input('Deseja sair do programa? [S/N]: ')).strip().upper()
        if continuar in 'Ss':
            print('\nSaindo do programa.\n')
            break
        else:
            os.system('cls')