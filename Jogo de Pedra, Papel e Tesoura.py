import random

while True:

  print('-~'*20)
  titulo = 'Jokenpô'
  print(f'{titulo:^40}')
  print('-~'*20)

  jogador = input('Escolhar Pedra, Papel ou Tesoura, para começar: ').lower()

  lista = ['pedra', 'papel', 'tesoura']
  maquina = random.choice(lista)

  if jogador not in lista:
      print('Escolha inválida!')
  else:
      if jogador == maquina:
        print('Empate!')
      elif (jogador == 'pedra' and maquina == 'tesoura') or (jogador == 'papel' and maquina == 'pedra') or (jogador == 'tesoura' and maquina == 'papel'):
        print(f'VOCÊ GANHOU! seu adversário escolheu {maquina}')
      else:
        print(f'VOCÊ PERDEU! seu adversário escolheu {maquina}')
  
  continuar = input('Deseja continuar o jogo? (sim/não): ')
  
  if continuar != 'sim':
     print('Saindo do Jogo')
     break 