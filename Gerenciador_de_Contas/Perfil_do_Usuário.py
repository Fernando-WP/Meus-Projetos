import customtkinter as ctk
from PIL import Image, ImageTk
import os

def perfil_do_usuário(usuário):
    janela_perfil = ctk.CTkToplevel()
    janela_perfil.title('Perfil do Usuário')
    janela_perfil.geometry('400x400')

    label_titulo = ctk.CTkLabel(janela_perfil, text='Perfil do Usuário', font=ctk.CTkFont(size=20, weight='bold'))
    label_titulo.pack(pady=10)

    caminho_imagem = 'perfil.png'
    if not os.path.exists(caminho_imagem):
        caminho_imagem = 'image_padrão.png'

    imagem = Image.open(caminho_imagem).resize((100, 100))
    imagem_tk = ctk.CTkImage(light_image=imagem, dark_image=imagem, size=(100, 100))
    label_imagem = ctk.CTkLabel(janela_perfil, image=imagem_tk, text='')
    label_imagem.pack(pady=10)

    ctk.CTkLabel(janela_perfil, text=f'Usuário: {usuário['Nome do Usuário']}', anchor='w', justify='left').pack(pady=5, fill='x', padx=20)
    ctk.CTkLabel(janela_perfil, text=f'Data de Nascimento: {usuário['Data de Nascimento']}', anchor='w', justify='left').pack(pady=5, fill='x', padx=20)
    ctk.CTkLabel(janela_perfil, text=f'Email: {usuário['Email']}', anchor='w', justify='left').pack(pady=5, fill='x', padx=20)
    ctk.CTkLabel(janela_perfil, text=f'Telefone: {usuário['Telefone']}', anchor='w', justify='left').pack(pady=5, fill='x', padx=20)
    ctk.CTkLabel(janela_perfil, text=f'Cidade: {usuário['Cidade']}', anchor='w', justify='left').pack(pady=5, fill='x', padx=20)