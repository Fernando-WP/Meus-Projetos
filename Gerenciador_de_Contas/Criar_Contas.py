import customtkinter as ctk
from tkinter import messagebox
from Gerenciador_de_Contas import Salvar_e_carregar_conta

conta = []

def janela_criar_conta(janela, conta):
    janela_criar_conta = ctk.CTkToplevel()
    janela_criar_conta.title('Criar Conta')
    janela_criar_conta.geometry('400x400')

    label_criar_conta = ctk.CTkLabel(janela_criar_conta, text='Criar Conta', font=ctk.CTkFont(size=20, weight='bold'))
    label_criar_conta.pack(pady=20)

    entry_nome_do_usuário = ctk.CTkEntry(janela_criar_conta, placeholder_text='Nome do Usuário')
    entry_nome_do_usuário.pack(pady=5)

    entry_data_de_nascimento = ctk.CTkEntry(janela_criar_conta, placeholder_text='(DD/MM/AAAA)')
    entry_data_de_nascimento.pack(pady=5)

    entry_email = ctk.CTkEntry(janela_criar_conta, placeholder_text='Email')
    entry_email.pack(pady=5)

    entry_senha = ctk.CTkEntry(janela_criar_conta, placeholder_text='Senha', show='*')
    entry_senha.pack(pady=5)

    entry_confirmar_senha = ctk.CTkEntry(janela_criar_conta, placeholder_text='Confirmar Senha', show='*')
    entry_confirmar_senha.pack(pady=5)

    entry_telefone = ctk.CTkEntry(janela_criar_conta, placeholder_text='Telefone')
    entry_telefone.pack(pady=5)

    entry_cidade = ctk.CTkEntry(janela_criar_conta, placeholder_text='Cidade')
    entry_cidade.pack(pady=5)

    def criar_conta():
        nome_do_usuário = entry_nome_do_usuário.get().strip()
        data_de_nascimento = entry_data_de_nascimento.get().strip()
        email = entry_email.get().strip()
        senha = entry_senha.get().strip()
        confirmar_senha = entry_confirmar_senha.get().strip()
        telefone = entry_telefone.get().strip()
        cidade = entry_cidade.get().strip()

        if not nome_do_usuário or not email or not senha or not confirmar_senha or not telefone or not cidade:
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
        
        if not re.match(r'^\d{2}/\d{2}/\d{4}$', data_de_nascimento):
            messagebox.showerror('Erro', 'A data de nascimento deve estar no formato DD/MM/AAAA!')
            return
        
        conta.append({
            'Nome do Usuário': nome_do_usuário,
            'Data de Nascimento': data_de_nascimento,
            'Email': email,
            'Senha': senha,
            'Telefone': telefone,
            'Cidade': cidade
        })

        Salvar_e_carregar_conta.salvar_contas(conta)

        messagebox.showinfo('Sucesso', 'Conta criada com sucesso!')
        janela_criar_conta.destroy()

    ctk.CTkButton(janela_criar_conta, text='Criar', command=criar_conta).pack(pady=20)