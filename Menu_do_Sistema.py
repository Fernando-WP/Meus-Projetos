import customtkinter as ctk
from Gerenciador_de_Contas import *

ctk.set_appearance_mode('light')
ctk.set_default_color_theme('blue')

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

botão_conta_criada = ctk.CTkButton(janela, text='Entra', command=lambda: conta_criada(entry_email_ou_usuário, entry_senha, conta))
botão_conta_criada.pack(pady=10)

botão_criar_conta = ctk.CTkButton(janela, text='Criar Conta', command=lambda: janela_criar_conta(janela, conta))
botão_criar_conta.pack(pady=10)

janela.mainloop()

