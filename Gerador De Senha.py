import random
import string
 
usuário = str(input('Digita seu usuário: '))

print('\033[1;34mVocê deseja cria uma senha aleatória? digita Sim.\033[m')

senha_do_usuário = (input('Digita sua senha: '))

def gerar_senha(tamanho:16):
    caracteiras = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteiras) for i in range(tamanho))
    return senha

senha_gerador = gerar_senha(8)

if senha_do_usuário in 'Sim':
 print(f'''\033[1;32mSeja Bem Vindo!\033[m
Seu usuário é: {usuário}
Sua senha é: {senha_gerador}''')
else:
  print(f'''\033[1;32mSeja Bem vindo!\033[m
Seu usuário é: {usuário}
Sua senha é: {senha_do_usuário}''')
