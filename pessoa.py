import random
import time
from pokemon import *

PAUSA = 3

NOMES = [
    'Misty', 'May', 'Dawn', 'Cilan', 'Íris', 'Serena', 'Chris', 'Max',
    'Dany', 'Clemont', 'Bonnie', 'Alexa', 'Lilian', 'George', 'Lulú',
    'Victória', 'Chloe', 'Gary', 'Ritchie', 'Vicent', 'Harrison', 'Morrison',
    'Tyson', 'Paul', 'Barry', 'Nando', 'Stephan', 'Cameron', 'Bianca', 'Aria'
]

POKEMONS = [
    PokemonFogo('Charmander'),
    PokemonFogo('Charmilion'),
    PokemonFogo('Charizard'),
    PokemonFogo('Flareon'),
    PokemonFogo('Entei'),
    PokemonEletrico('Pikachu'),
    PokemonEletrico('Pichu'),
    PokemonEletrico('Raichu'),
    PokemonEletrico('Electabuzz'),
    PokemonEletrico('Raikou'),
    PokemonAgua('Squirtle'),
    PokemonAgua('Wartortle'),
    PokemonAgua('Blastoise'),
    PokemonAgua('Vaporeon'),
    PokemonAgua('Sharpedo'),
    PokemonPlanta('Bulbasaur'),
    PokemonPlanta('Ivysaur'),
    PokemonPlanta('Venusaur'),
    PokemonPlanta('Grovyle'),
    PokemonPlanta('Zarude'),
    PokemonVoador('Pidgey'),
    PokemonVoador('Pidgeotto'),
    PokemonVoador('Pidgeot'),
    PokemonVoador('Spearow'),
    PokemonVoador('Braviary'),
    PokemonPedra('Rolycoly'),
    PokemonPedra('Carkol'),
    PokemonPedra('Coalossoal'),
    PokemonPedra('Dreadnaw'),
    PokemonPedra('Rhyhron'),
    PokemonPsiquico('Abra'),
    PokemonPsiquico('Kadabra'),
    PokemonPsiquico('Alakazam'),
    PokemonPsiquico('Hypno'),
    PokemonPsiquico('Mewtwo'),
    PokemonDragao('Rayquaza'),
    PokemonDragao('Giratina'),
    PokemonDragao('Zekrom'),
    PokemonDragao('Dragonite'),
    PokemonDragao('Salamence'),
    PokemonSombrio('Poochyena'),
    PokemonSombrio('Mightyena'),
    PokemonSombrio('Umbreon'),
    PokemonSombrio('Houndourn'),
    PokemonSombrio('Houndoom'),
    PokemonFada('Clefairy'),
    PokemonFada('Clefable'),
    PokemonFada('Jigglypuff'),
    PokemonFada('Wigglytuff'),
    PokemonFada('Mr. Mime'),
]

class Pessoa:

    def __init__(self, nome=None, pokedex=[], dinheiro=100):
        if nome:
            self.nome = nome
        else:
            self.nome = random.choice(NOMES)

        self.pokedex = pokedex

        self.dinheiro = dinheiro

    def __str__(self):
        return self.nome

    def mostrar_pokemons(self):
        if self.pokedex:
            print('Pokedex de {}: '.format(self))
            for index, pokemon in enumerate(self.pokedex):
                print('{}: {}'.format(index+1, pokemon))
        else:
            print('A Pokedex de {} está vazia\n'.format(self))

    def escolher_pokemon(self):
        if self.pokedex:
            pokemon_escolhido = random.choice(self.pokedex)
            print('{} escolheu {}\n'.format(self, pokemon_escolhido))
            return pokemon_escolhido
        else:
            print(':( A pokedex de {} está vazia\n'.format(self))

    def mostrar_dinheiro(self):
        print('{} possui $ {} em sua conta'.format(self, self.dinheiro))

    def ganhar_dinheiro(self, quantiade):
        self.dinheiro += quantiade
        print('{} ganhou $ {}'.format(self, quantiade))

    def batalhar(self, pessoa):
        print('{} iniciou uma batalha com {} \n'.format(self, pessoa))

        pessoa.mostrar_pokemons()
        pokemon_inimigo = pessoa.escolher_pokemon()

        pokemon = self.escolher_pokemon()

        if pokemon and pokemon_inimigo:
            while True:
                vitoria = pokemon.atacar(pokemon_inimigo)
                time.sleep(PAUSA)
                if vitoria:
                    print('{} ganhou a batalha!\n'.format(self))
                    self.ganhar_dinheiro(pokemon_inimigo.level * 100)
                    break

                vitoria_inimiga = pokemon_inimigo.atacar(pokemon)
                time.sleep(PAUSA)
                if vitoria_inimiga:
                    print('{} ganhou a batalha!\n'.format(pessoa))
                    break

        else:
            print('Essa batalha não pode ocorrer!\n')

class Player(Pessoa):
    tipo = 'Player'

    def capturar(self, pokemon):
        self.pokedex.append(pokemon)
        print('{} capturou {}!\n'.format(self, pokemon))

    def escolher_pokemon(self):
        self.mostrar_pokemons()

        if self.pokedex:
            while True:
                escolha = input('Escolha seu Pokémon: ')
                try:
                    escolha = int(escolha)
                    pokemon_escolhido = self.pokedex[escolha-1]
                    print('{} eu escolho você!!\n'.format(pokemon_escolhido))
                    return pokemon_escolhido
                except:
                    print('Escolha inválida!')
        else:
            print(':( A pokedex de {} está vazia\n'.format(self))

    def explorar(self):
        if random.random() <= 0.3:
            pokemon = random.choice(POKEMONS)
            print('Um pokémon selvagem foi encontrado: {}'.format(pokemon))

            escolha = input('Deseja captura-lo?[s/n]: ')
            if escolha == 's' or escolha == 'S':
               if random.random() >= 0.5:
                   self.capturar(pokemon)
               else:
                   print('{} fugiu!\n'.format(pokemon))
            else:
                print('Ok! Boa viagem!\n')

        else:
            print('A exploração não gerou resulados!\n')


class Inimigo(Pessoa):
    tipo = 'Inimigo'

    def __init__(self, nome=None, pokedex=None):
        if not pokedex:
            pokemons_aleatorios = []
            for i in range(random.randint(1, 6)):
                pokemons_aleatorios.append(random.choice(POKEMONS))

            super().__init__(nome=nome, pokedex=pokemons_aleatorios)
        else:
            super().__init__(nome=nome, pokedex=pokedex)