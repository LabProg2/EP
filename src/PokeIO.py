from Stats import Stats
from Move import Move
from Type import Type
from Pokemon import Pokemon
class PokeIO:
    ''' 
    This class is responsible for every interaction between user and this pokemon game
    '''
    def read_poke(self, poke_path):
        if type(poke_path) is not str:
            raise TypeError("poke_path must be a string")
        try:
            poke_file = open(poke_path, 'r')
        except FileNotFoundError:
            print("The pokemon file couldn't be read")
            raise FileNotFoundError

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

    def read_move(self, upper_limit = 10, restriction_list = []):
        ''' Reads a movement from the users keyboard
        :param upper_limit: The upper limit for the number entry
        :param restriction_list: Restrictions for the number entry
        :returns: An integer representing the movement the user selected
        '''
        if not isinstance(restriction_list, list):
            raise TypeError("Restriction list for moves must be a list")
        for x in restriction_list:
            if type(x) is not int:
                raise TypeError("Each element of restriction list for moves must be an integer")

        if len(restriction_list) == 0 and upper_limit > 0:
            restriction_list = list(range(1, upper_limit + 1))

        x = None 
        while x not in restriction_list or type(x) is not int:
            s = input()
            try:
                x = int(s)
            except: 
                pass
            if x not in restriction_list or type(x) is not int:
                print("Por favor, seja bonzinho e digite um movimento válido.")
        return x - 1
                
    def print_move_list(self, move_list):
        ''' Prints the list of movements a pokemon can make
        :param move_list: The list of movements thats going to be printed
        '''
        if not isinstance(move_list, list):
            raise TypeError("Move list for moves must be a list")
        for x in move_list:
            if not isinstance(x, Move) is not int:
                raise TypeError("Each element of the move list must be of type Move")
        
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
        if not isinstance(is_on_turn, bool):
            raise TypeError("is_on_turn must be a bool instance")
        if not isinstance(pokemon, Pokemon):
            raise TypeError("pokemon must be a Pokemon instance")

        print(pokemon.name + " HP: " + str(pokemon.hp), end = "")
        if is_on_turn:
            print(" [Em sua vez]")
        print('')
