class PokeIO:
    ''' 
    This class is responsible for every interaction between user and this pokemon game
    '''
    def read_move(upper_limit, restriction_list = []):
        ''' Reads a movement from the users keyboard
        :param upper_limit: The upper limit for the number entry
        :param restriction_list: Restrictions for the number entry
        :returns: An integer representing the movement the user selected
        '''
        #aqui preicsa dar uns rise violento
        x = None
        while x in restriction_list or type(x) is not int:
            s = input("Escolha seu movimento!")
            try:
                x = int(s)
            except: 
                pass
            if x in restriction_list or type(x) is not int:
                print("Por favor, seja bonzinho e digite um movimento válido.")
        return x #+ 1 ou não? hehe acho que sim
                
    def print_move_list(move_list):
        ''' Prints the list of movements a pokemon can make
        :param move_list: The list of movements thats going to be printed
        '''
        #precisa dar uns rise aqui
        i = 1
        for move in move_list:
            print("[" + i + "] - " + move.name + " (" + move.pp + ")")
            i = i + 1

    def print_poke_info(pokemon, is_on_turn = False):
        ''' Prints the info of a pokemon
        :param pokemon: The pokemon that will have its info printed
        :param is_on_turn: A flag to inform if the pokemon is on its is_on_turn
        '''
        #precisa dar uns dois rise aqui
        print(pokemon.name + "HP: " + pokemon.stats.hp, end = " ")
        if is_on_turn:
            print("[Em sua vez]", end = "")