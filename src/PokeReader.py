from Pokemon import Pokemon
from sys import stdin
from Type import Type
from Move import Move
from Stats import Stats

class PokeReader:
    '''This class reads two pokemons from the standart in'''
    def read_pokemons(self, n = 2):
        pokemon_list = []
        for _ in range (n):
            pokemon_list.append(self.read_pokemon())
        return tuple(pokemon_list)

    def read_pokemon(self):     
        name = stdin.readline()
        try:
            lvl = stdin.readline()
        except ValueError:
            raise ValueError("Level must be an integer")
        try:
            hp = stdin.readline()
        except ValueError:
            raise ValueError("Health powe must be an integer")
        try:
            atk = stdin.readline()
        except ValueError:
            raise ValueError("Attack must be an integer")
        try:
            defe = int(stdin.readline())
        except ValueError:
            raise ValueError("Defence must be an integer")
        try:
            spd = int(stdin.readline())
        except ValueError:
            raise ValueError("Speed must be an integer")
        try:
            spc = int(stdin.readline())
        except ValueError:
            raise ValueError("Special must be an integer")
        try:
            tp = int(stdin.readline())
            typ1 = Type(tp)
            tp = int(stdin.readline())
            typ2 = Type(tp)
        except ValueError:
            raise ValueError("Pokemon Type must be an integer")
        typ_list = [typ1, typ2]
        nat = stdin.readline()
        stats = Stats(hp, atk, defe, spd, spc)
        move_list = []
        for i in range(int(nat)):
            move_name = stdin.readline()
            try:
                tp = int(stdin.readline())
                move_type = Type(tp)
            except ValueError:
                raise ValueError("A move type must be an integer")
            try:
                move_acu = int(stdin.readline())
            except ValueError:
                raise ValueError("A move accuracy must be an integer")
            try:
                move_pwr = int(stdin.readline())
            except ValueError:
                raise ValueError("A move power must be an integer")
            try:
                move_pp = int(stdin.readline())
            except ValueError:
                raise ValueError("A move pp must be an integer")
            move = Move(move_name, move_type, move_acu, move_pwr, move_pp)
            move_list.append(move)
        return Pokemon(typ_list, stats, move_list, name, lvl)
