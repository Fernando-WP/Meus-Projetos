import customtkinter as ctk
from tkinter import messagebox

ctk.set_appearance_mode('light')
ctk.set_default_color_theme('blue')

conta = []

def carregar_contas():
    try:
        with open('contas.txt', 'r') as f:
            for linha in f:
                dados = linha.strip().split('|')
                if len(dados) == 5:
                    conta.append({
                        'Nome do Usuário': dados[0],
                        'Email': dados[1],
                        'Senha': dados[2],
                        'CEP': dados[3],
                        'Número da Casa': dados[4]
                    })
    except FileNotFoundError:
        with open('contas.txt', 'w') as f:
            pass
    return conta

def salvar_contas():
    with open('contas.text', 'w') as f:
        for c in conta:
            f.write(f'{c['Nome do Usuário']}|{c['Email']}|{c['Senha']}|{c['CEP']}|{c['Número da Cesa']}\n')

def conta_criada():
    entrada = entry_email_ou_usuário.get().strip()
    senha = entry_senha.get().strip()

    if not entrada or not senha:
        messagebox.showerror('Erro', 'Preencha todos os campos!')
        return
    
    if len(senha) < 6:
        messagebox.showerror('Erro', 'A senha deve ter pelo menos 6 caracteres!')
        return

    entrada = entrada.strip().lower()

    for c in conta:
        nome_usuário = c.get('Nome do Usuário').strip().lower()
        email = c.get('Email').strip().lower()
        senha_cadastrada = c.get('Senha')

        if (entrada == nome_usuário or entrada == email) and senha == senha_cadastrada:
            messagebox.showinfo('Sucesso', f'Bem-vindo {c.get('Nome do Usuário')}!')
            return
        
    messagebox.showerror('Erro', 'CONTA NÃO ENCONTRADA: Verifique o nome de usuário ou email e senha digitados!')

def janela_criar_conta():
    janela_criar_conta = ctk.CTkToplevel()
    janela_criar_conta.title('Criar Conta')
    janela_criar_conta.geometry('400x400')

    label_criar_conta = ctk.CTkLabel(janela_criar_conta, text='Criar Conta', font=ctk.CTkFont(size=20, weight='bold'))
    label_criar_conta.pack(pady=20)

    entry_nome_do_usuário = ctk.CTkEntry(janela_criar_conta, placeholder_text='Nome do Usuário')
    entry_nome_do_usuário.pack(pady=5)

    entry_email = ctk.CTkEntry(janela_criar_conta, placeholder_text='Email')
    entry_email.pack(pady=5)

    entry_senha = ctk.CTkEntry(janela_criar_conta, placeholder_text='Senha', show='*')
    entry_senha.pack(pady=5)

    entry_confirmar_senha = ctk.CTkEntry(janela_criar_conta, placeholder_text='Confirmar Senha', show='*')
    entry_confirmar_senha.pack(pady=5)

    entry_cep = ctk.CTkEntry(janela_criar_conta, placeholder_text='CEP')
    entry_cep.pack(pady=5)

    entry_números_da_casa = ctk.CTkEntry(janela_criar_conta, placeholder_text='Número da Casa')
    entry_números_da_casa.pack(pady=5)

    def criar_conta():
        nome_do_usuário = entry_nome_do_usuário.get().strip()
        email = entry_email.get().strip()
        senha = entry_senha.get().strip()
        confirmar_senha = entry_confirmar_senha.get().strip()
        cep = entry_cep.get().strip()
        números_da_casa = entry_números_da_casa.get().strip()

        if not nome_do_usuário or not email or not senha or not confirmar_senha or not cep or not números_da_casa:
            messagebox.showerror('Erro', 'Preencha todos os campos!')
            return
        
        import re
        if not re.match(r'^[A-Za-z0-9_.-]+$', nome_do_usuário):
            messagebox.showerror('Erro', 'O nome de usuário deve conter apenas letras, números, pontos, sublinhados e hífens!')
            return
        
        for c in conta:
            if c['Nome do Usuário'].strip().lower() == nome_do_usuário:
                messagebox.showerror('Erro', 'Nome de usuário já existe!')
                return
            
        if '@' not in email:
            messagebox.showerror('Erro', 'O campo deve conter um e-mail válido!')
            return
        
        if len(senha) < 6:
            messagebox.showerror('Error', 'A senha deve ter pelo menos 6 caracteres!')
            return
        
        if senha != confirmar_senha:
            messagebox.showerror('Erro', 'As senhas não coincidem!')
            return
        
        if not cep.isdigit() or len(cep) != 8:
            messagebox.showerror('Erro', 'CEP deve conter 8 dígitos!')
            return
        
        if not números_da_casa.isdigit():
            messagebox.showerror('Erro', 'Número da casa deve conter somente números')
            return
        
        conta.append({
            'Nome do Usuário': nome_do_usuário,
            'Email': email,
            'Senha': senha,
            'CEP': cep,
            'Números da Casa': números_da_casa
        })

        salvar_contas()

        messagebox.showinfo('Sucesso', 'Conta criada com sucesso!')
        janela_criar_conta.destroy()

    ctk.CTkButton(janela_criar_conta, text='Criar', command=criar_conta).pack()

conta = carregar_contas()

janela = ctk.CTk()
janela.title('Login de Conta')
janela.geometry('400x400')

label_titulo = ctk.CTkLabel(janela, text='Login de Conta', font=ctk.CTkFont(size=20, weight='bold'))
label_titulo.pack(pady=10)

entry_email_ou_usuário = ctk.CTkEntry(janela, placeholder_text='Email ou Usuário')
entry_email_ou_usuário.pack(pady=9)

entry_senha = ctk.CTkEntry(janela, placeholder_text='Senha', show='*')
entry_senha.pack(pady=9)

botão_conta_criada = ctk.CTkButton(janela, text='Entra', command=conta_criada)
botão_conta_criada.pack(pady=10)

botão_criar_conta = ctk.CTkButton(janela, text='Criar Conta', command=janela_criar_conta)
botão_criar_conta.pack(pady=10)

janela.mainloop()