from Stats import Stats
from Move import Move
from Pokemon import Pokemon
from movelist import MoveList

class BattleIO:
    ''' 
    This class is responsible for every interaction between the battle and the user
    '''
    def read_move_of(self, pokemon):
        ''' Reads a movement from the users keyboard

        :param pokemon: The pokemon that is going the perform the next attack
        :returns: An integer representing the movement the user selected
        '''
        if not isinstance(pokemon, Pokemon):
            raise TypeError("pokemon must be an instance of Pokemon")

        if not pokemon.moves.has_available_moves():
            return pokemon.moves.struggle

        x = input()
        try:
            x = int(x)
        except:
            pass
        while not isinstance(x, int) or not pokemon.moves.is_move_available(x):
            print("Please, be a good boy and choose a valid movement")
            x = input()
            try:
                x = int(x)
            except: 
                pass
        return pokemon.moves.get_move(x)
                
    def print_moves_of(self, pokemon):
        ''' Prints the list of movements a pokemon can make

        :param move_list: The list of movements thats going to be printed
        '''
        if not isinstance(pokemon, Pokemon):
            raise TypeError("pokemon must be an instance of Pokemon")
        
        print("Choose your move:")
        for i, move in pokemon.moves.enumerate():
            print("[" + str(i) + "] - " + move.name + " (" + str(move.pp) + ")")

    def print_poke_info(self, pokemon, is_on_turn = False):
        ''' Prints the info of a pokemon

        :param pokemon: The pokemon that will have its info printed
        :param is_on_turn: A flag to inform if the pokemon is on its is_on_turn
        '''
        try:
            is_on_turn = bool(is_on_turn)
        except TypeError:
            raise TypeError("is_on_turn must be a bool")

        if not isinstance(pokemon, Pokemon):
            raise TypeError("pokemon must be a Pokemon instance")

        print(pokemon.name + " HP: " + str(pokemon.hp), end = "")
        if is_on_turn:
            print(" [Em sua vez]")
        print('')

    def print_move_result(self, atking_poke, move, damage):
        ''' Prints the result of using a move anda cause a damage

        :param atking_poke: the pokemon that is attacking
        :param move: the move that the pokemon is using
        :param damage: the damage the pokemon caused
        '''
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
