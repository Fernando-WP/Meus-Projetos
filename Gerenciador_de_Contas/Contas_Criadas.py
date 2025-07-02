from tkinter import messagebox
from Gerenciador_de_Contas import Perfil_do_Usuário

conta = []

def conta_criada(entry_email_ou_usuário, entry_senha, conta):
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
            Perfil_do_Usuário.perfil_do_usuário(c)
            return
        
    messagebox.showerror('Erro', 'CONTA NÃO ENCONTRADA: Verifique o nome de usuário ou email e senha digitados!')