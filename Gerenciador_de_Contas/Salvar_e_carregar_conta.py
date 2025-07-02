def carregar_contas():
    contas = []
    try:
        with open('contas.txt', 'r') as f:
            for linha in f:
                dados = linha.strip().split('|')
                if len(dados) == 6:
                    contas.append({
                        'Nome do Usuário': dados[0],
                        'Data de Nascimento': dados[1],
                        'Email': dados[2],
                        'Senha': dados[3],
                        'Telefone': dados[4],
                        'Cidade': dados[5]
                    })
    except FileNotFoundError:
        pass
    return contas

def salvar_contas(contas):
    with open('contas.txt', 'w') as f:
        for c in contas:
            f.write(f'{c['Nome do Usuário']}|{c['Data de Nascimento']}|{c['Email']}|{c['Senha']}|{c['Telefone']}|{c['Cidade']}\n')