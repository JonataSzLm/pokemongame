import random

class Pokemon:

    def __init__(self, especie, level=None, nome=None):
        self.especie = especie

        if level:
            self.level = level
        else:
            self.level = random.randint(1, 100)

        if nome:
            self.nome = nome
        else:
            self.nome = especie

        self.ataque = self.level * 5
        self.vida = self.level * 10


    def __str__(self):
        return '{} [lv. {}]'.format(self.nome, self.level)

    def atacar(self, pokemon):
        ataque_efetivo = int(self.ataque * random.random() * 1.3)
        pokemon.vida -= ataque_efetivo

        print('{} perdeu {} pontos de vida'.format(pokemon, ataque_efetivo))

        if pokemon.vida <= 0:
            print('{} foi derrotado! \n'.format(pokemon))
            return True
        else:
            return False


class PokemonEletrico(Pokemon):

    tipo = 'Elétrico'

    def atacar(self, pokemon):
        print('{} lançou um raio do trovão em {}!'.format(self, pokemon))
        return super().atacar(pokemon)


class PokemonFogo(Pokemon):

    tipo = 'Fogo'

    def atacar(self, pokemon):
        print('{} lançou uma bola de fogo em {}!'.format(self, pokemon))
        return super().atacar(pokemon)


class PokemonAgua(Pokemon):

    tipo = 'Água'

    def atacar(self, pokemon):
        print('{} lançou um jato de água em {}!'.format(self, pokemon))
        return super().atacar(pokemon)

class PokemonPlanta(Pokemon):

    tipo = 'Planta'

    def atacar(self, pokemon):
        print('{} lançou uma chuva de sementes em {}!'.format(self, pokemon))
        return super().atacar(pokemon)

class PokemonVoador(Pokemon):

    tipo = 'Voador'

    def atacar(self, pokemon):
        print('{} lançou um furacão em {}!'.format(self, pokemon))
        return super().atacar(pokemon)

class PokemonPedra(Pokemon):

    tipo = 'Pedra'

    def atacar(self, pokemon):
        print('{} lançou um deslisamento de pedras em {}!'.format(self, pokemon))
        return super().atacar(pokemon)

class PokemonPsiquico(Pokemon):

    tipo = 'Psíquico'

    def atacar(self, pokemon):
        print('{} lançou um choque psíquico em {}!'.format(self, pokemon))
        return super().atacar(pokemon)

class PokemonDragao(Pokemon):

    tipo = 'Dragão'

    def atacar(self, pokemon):
        print('{} lançou um bafo de dragão em {}!'.format(self, pokemon))
        return super().atacar(pokemon)

class PokemonSombrio(Pokemon):

    tipo = 'Sombrio'

    def atacar(self, pokemon):
        print('{} lançou um pulso escuro em {}!'.format(self, pokemon))
        return super().atacar(pokemon)

class PokemonFada(Pokemon):

    tipo = 'Fada'

    def atacar(self, pokemon):
        print('{} lançou uma explosão lunar em {}!'.format(self, pokemon))
        return super().atacar(pokemon)

