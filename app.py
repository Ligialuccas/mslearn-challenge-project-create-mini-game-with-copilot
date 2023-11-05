# jogo papel, pedra e tesoura

# importar o modulo random
import random

options = ['pedra', 'papel', 'tesoura'] # lista de opções
score = 0
rounds_played = 0

while True:
    random_choice = random.choice(options) # escolha aleatória
    player_choice = input('Escolha entre pedra, papel ou tesoura: ') # escolha do jogador

    # se o meu jogador escolher pedra
    if player_choice == 'pedra':
        rounds_played += 1
        print('O computador escolheu:', random_choice)
        
        if random_choice == 'pedra':
            print('Empate!')
        elif random_choice == 'papel':
            print('Você perdeu!')
        elif random_choice == 'tesoura':
            print('Você ganhou!')
            score += 1

    # se o meu jogador escolher papel
    elif player_choice == 'papel':
        rounds_played += 1
        print('O computador escolheu:', random_choice)

        if random_choice == 'pedra':
            print('Você ganhou!')
            score += 1
        elif random_choice == 'papel':
            print('Empate!')
        elif random_choice == 'tesoura':
            print('Você perdeu!')

    # se o meu jogador escolher tesoura
    elif player_choice == 'tesoura':
        rounds_played += 1
        print('O computador escolheu:', random_choice)

        if random_choice == 'pedra':
            print('Você perdeu!')
        elif random_choice == 'papel':
            print('Você ganhou!')
            score += 1
        elif random_choice == 'tesoura':
            print('Empate!')

    # se o meu jogador escolher algo diferente de pedra, papel ou tesoura
    else:
        play_again = input('Deseja jogar novamente? (s/n) ')
        if play_again == 's':
            continue
        elif play_again == 'n':
            print('Você ganhou:', score, 'vezes!',rounds_played ,'rodadas jogadas!')
            break
        else:
            print('Escolha inválida!')
