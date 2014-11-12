from Stats import Stats
from Move import Move
from Pokemon import Pokemon
class BattleIO:
    ''' 
    This class is responsible for every interaction between the battle and the user
    '''
    def read_move(self, move_list):
        ''' Reads a movement from the users keyboard

        :param move_list: The move_list from which the user must choose a attack
        :returns: An integer representing the movement the user selected
        '''
        if not isinstance(move_list, list):
            raise TypeError("Move list for moves must be a list")
        for x in move_list:
            if not isinstance(x, Move):
                raise TypeError("Each element of the move list must be of type Move")
        
        available_list = []
        for i, move in enumerate(move_list):
            if i > 0 and move.pp != 0:
                available_list.append(i)

        if available_list == []:
            # the struggle
            return move_list[0]

        x = input()
        try:
            x = int(x)
        except:
            pass
        while x not in available_list or type(x) is not int:
            print("Please, be a good boy and choose a valid movement")
            x = input()
            try:
                x = int(x)
            except: 
                pass
        return move_list[x]
                
    def print_move_list(self, move_list):
        ''' Prints the list of movements a pokemon can make

        :param move_list: The list of movements thats going to be printed
        '''
        if not isinstance(move_list, list):
            raise TypeError("Move list for moves must be a list")
        for x in move_list:
            if not isinstance(x, Move):
                raise TypeError("Each element of the move list must be of type Move")
        
        print("Choose your move:")
        for i, move in enumerate(move_list):
            if i > 0:
                print("[" + str(i) + "] - " + move.name + " (" + str(move.pp) + ")")

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

    def print_move_result(self, atking_poke, move, damage):
        print(atking_poke.name, "used", move.name)
        if damage == -1:
            print("The attack was missed\n")
        else:
            print("It caused a damage of " + str(damage) + "\n") 

    def print_winner(self, pokemon):
        ''' Prints the winner pokemon
        :param pokemon: The winner pokemon
        '''

        if not isinstance(pokemon, Pokemon):
            raise TypeError("pokemon must be a Pokemon instance")

        print(pokemon.name + " is the winner!")