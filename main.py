import pickle
import time
from pokemon import *
from pessoa import *

PAUSA = 1

def escolher_pokemon_inicial(player):

    squirtle = PokemonAgua('Squirtle', level=1)
    charmander = PokemonFogo('Charmander', level=1)
    bulbasaur = PokemonPlanta('Bulbasaur', level=1)

    print('')
    print('Você tem três opções: ')
    print('1: ', squirtle)
    print('2: ', charmander)
    print('3: ', bulbasaur)

    while True:
        escolha = input('Escolha seu Pokémon: ')

        if escolha == '1':
            player.capturar(squirtle)
            break
        elif escolha == '2':
            player.capturar(charmander)
            break
        elif escolha == '3':
            player.capturar(bulbasaur)
            break
        else:
            print('')
            print('Escolha invalida!\n')

def salvar_jogo(player):
    try:
        with open('database.db', 'wb') as arquivo:
            pickle.dump(player, arquivo)
            print('*** Jogo salvo com sucesso! ;) ***\n')
    except Exception as e:
        print('*** Erro ao salvar o jogo! :( ***\n')
        print(e)

def carregar_jogo():
    try:
        with open('database.db', 'rb') as arquivo:
            player = pickle.load(arquivo)
            return player
    except:
        print('*** Não há dados salvos ***\n')


if __name__ == "__main__":

    print('***************************************************')
    print('Bem Vindo ao game Pokémon RPG de terminal!')
    print('***************************************************\n')
    time.sleep(PAUSA)

    player_temp = carregar_jogo()

    if player_temp:
        print('*** Verificamos que há uma campanha salva no nome: {} ***'.format(player_temp))
        reposta = input('você gostaria de continuar? [s/n]:')
        if reposta == 's' or reposta == 'S':
            player = player_temp
            time.sleep(PAUSA)
            print('')
            print('*** Jogo carregado com sucesso! ;) ***\n')
        else:
            player = None

    if not player:
        time.sleep(PAUSA)
        print('\n')
        print('Olá! Eu sou o professor Ash')
        nome = input('Qual é o seu nome? ')
        player = Player(nome)
        time.sleep(PAUSA)
        print('****************************************************\n')
        print('{}, esse é um mundo habitado por pokémons, a partir de agora a sua missão é se tornar um mestre de pokémons'.format(nome))
        print('Capture o maximo de pokémons que conseguir e lute com seus inimigos...')
        print('*****************************************************\n')
        time.sleep(PAUSA)

        if player.pokedex:
            print('Já vi que você possuí alguns pokémons!')
        else:
            print('Você não possuí nenhum pokémon, portanto precisa escolher um: \n')
            escolher_pokemon_inicial(player)

        ash = Inimigo('Ash', pokedex=[PokemonEletrico('Lapras', level=1)])
        time.sleep(PAUSA)
        print('Vamos testar suas habilidades, batalhe comigo!')
        player.batalhar(ash)


    while True:
        time.sleep(PAUSA)
        print('')
        print('*************************************')
        print('O que deseja fazer?')
        print('1: Explorar o mundo a procura de pokémons')
        print('2: Ir para o ginásio para uma batalha aleatória')
        print('3: Ver seu saldo')
        print('4: Ver sua Pokédex')
        print('5: Salvar campanha')
        print('6: Carregar campanha salva')
        print('0: Sair do jogo :(')
        print('*************************************\n')

        escolha = input('Sua escolha: ')

        if escolha == '0':
            print('*** Fim de Jogo! ***')
            break
        elif escolha == '1':
            player.explorar()
            time.sleep(PAUSA)
        elif escolha == '2':
            inimigo_aleatorio = Inimigo()
            player.batalhar(inimigo_aleatorio)
            time.sleep(PAUSA)
        elif escolha == '3':
            player.mostrar_dinheiro()
            time.sleep(PAUSA)
        elif escolha == '4':
            player.mostrar_pokemons()
            time.sleep(PAUSA)
        elif escolha == '5':
            salvar_jogo(player)
            time.sleep(PAUSA)
        elif escolha == '6':
            campanha = carregar_jogo()
            if campanha:
                print('\n')
                print('Há uma campanha salva no nome: {}'.format(campanha))
                confirma = input('Você deseja sobrescrever a campanha atual? [s/n]: ')
                if confirma == 's' or confirma == 'S':
                    player = campanha
                    time.sleep(PAUSA)
                    print('*** Jogo carregado com sucesso! ;) ***\n')
                else:
                    time.sleep(PAUSA)
                    print('Ok! vamos continuar como {}...'.format(player))
            else:
                time.sleep(PAUSA)
                print('*** Não há dados salvos! :( ***\n')
        else:
            time.sleep(PAUSA)
            print('*** Escolha inválida! ***\n')


        if player.dinheiro >= 1000000:
            player.mostrar_dinheiro()
            print('\n')
            time.sleep(PAUSA*2)
            print('*** Você ficou rico e resolveu se aposentar das batalhas de pokémons ;) ***')
            print('*** Fim! ***')
            print('*****************************************************************************\n')
            break

