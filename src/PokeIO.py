from Stats import Stats
from Move import Move
from Type import Type
from Pokemon import Pokemon
class PokeIO:
    ''' 
    This class is responsible for every interaction between user and this pokemon game
    '''
    def read_poke(self, poke_file):
        name = poke_file.readline()
        try:
            lvl = poke_file.readline()
        except ValueError:
            print("Level must be an integer")
        try:
            hp = poke_file.readline()
        except ValueError:
            print("Health powe must be an integer")
        try:
            atk = poke_file.readline()
        except ValueError:
            print("Attack must be an integer")
        try:
            defe = int(poke_file.readline())
        except ValueError:
            print("Defence must be an integer")
        try:
            spd = int(poke_file.readline())
        except ValueError:
            print("Speed must be an integer")
        try:
            spc = int(poke_file.readline())
        except ValueError:
            print("Special must be an integer")
        try:
            tp = int(poke_file.readline())
            typ1 = Type(tp)
            tp = int(poke_file.readline())
            typ2 = Type(tp)
        except ValueError:
            print("Pokemon Type must be an integer")
        typ_list = [typ1, typ2]
        nat = poke_file.readline()
        stats = Stats(hp, atk, defe, spd, spc)
        move_list = []
        for i in range(int(nat)):
            move_name = poke_file.readline()
            try:
                tp = int(poke_file.readline())
                move_type = Type(tp)
            except ValueError:
                print("A move type must be an integer")
            try:
                move_acu = int(poke_file.readline())
            except ValueError:
                print("A move accuracy must be an integer")
            try:
                move_pwr = int(poke_file.readline())
            except ValueError:
                print("A move power must be an integer")
            try:
                move_pp = int(poke_file.readline())
            except ValueError:
                print("A move pp must be an integer")
            move = Move(move_name, move_type, move_acu, move_pwr, move_pp)
            move_list.append(move)
        return Pokemon(typ_list, stats, name, lvl, move_list)

    def read_move(self, move_list):
        ''' Reads a movement from the users keyboard
        :param move_list: The move_list from which the user must choose a attack
        :returns: An integer representing the movement the user selected
        '''
        available_list = []
        for i, move in enumerate(move_list):
            if move.pp != 0:
                available_list.append(i + 1)

        print(available_list)

        #aqui preicsa dar uns rise violento
        x = int(input())
        while x not in available_list or type(x) is not int:
            print("Por favor, seja bonzinho e digite um movimento válido.")
            x = input()
            try:
                x = int(x)
            except: 
                pass
        return move_list[x - 1] #+ 1 ou não? hehe acho que sim
                
    def print_move_list(self, move_list):
        ''' Prints the list of movements a pokemon can make
        :param move_list: The list of movements thats going to be printed
        '''
        #precisa dar uns rise aqui
        print("Choose your move:")
        i = 1
        for move in move_list:
            print("[" + str(i) + "] - " + move.name + " (" + str(move.pp) + ")")
            i = i + 1

    def print_poke_info(self, pokemon, is_on_turn = False):
        ''' Prints the info of a pokemon
        :param pokemon: The pokemon that will have its info printed
        :param is_on_turn: A flag to inform if the pokemon is on its is_on_turn
        '''
        #precisa dar uns dois rise aqui
        print(pokemon.name + " HP: " + str(pokemon.hp), end = "")
        if is_on_turn:
            print(" [Em sua vez]")
        print('')
