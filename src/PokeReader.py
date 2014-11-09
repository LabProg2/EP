from Pokemon import Pokemon
from sys import stdin
from Type import Type
from Move import Move
from Stats import Stats

class PokeReader:
    '''This class reads two pokemons from the standart in'''
    def read_pokemons(self):
        pokemon1 = self.read_pokemon()
        pokemon2 = self.read_pokemon()
        return (pokemon1, pokemon2)

    def read_pokemon(self):     
        name = stdin.readline()
        try:
            lvl = stdin.readline()
        except ValueError:
            print("Level must be an integer")
        try:
            hp = stdin.readline()
        except ValueError:
            print("Health powe must be an integer")
        try:
            atk = stdin.readline()
        except ValueError:
            print("Attack must be an integer")
        try:
            defe = int(stdin.readline())
        except ValueError:
            print("Defence must be an integer")
        try:
            spd = int(stdin.readline())
        except ValueError:
            print("Speed must be an integer")
        try:
            spc = int(stdin.readline())
        except ValueError:
            print("Special must be an integer")
        try:
            tp = int(stdin.readline())
            typ1 = Type(tp)
            tp = int(stdin.readline())
            typ2 = Type(tp)
        except ValueError:
            print("Pokemon Type must be an integer")
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
                print("A move type must be an integer")
            try:
                move_acu = int(stdin.readline())
            except ValueError:
                print("A move accuracy must be an integer")
            try:
                move_pwr = int(stdin.readline())
            except ValueError:
                print("A move power must be an integer")
            try:
                move_pp = int(stdin.readline())
            except ValueError:
                print("A move pp must be an integer")
            move = Move(move_name, move_type, move_acu, move_pwr, move_pp)
            move_list.append(move)
        #stdin.close()
        return Pokemon(typ_list, stats, move_list, name, lvl)