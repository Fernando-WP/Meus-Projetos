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

menu_de_opções()
escolhar_de_opções = int(input('Escolha uma das opção: '))