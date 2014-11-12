import sys
from Battle import Battle
from ServerBattle import ServerBattle
from PokeReader import PokeReader
from sys import argv

pokereader = PokeReader()
if argv[1] == "-s":
    server_poke = pokereader.read_pokemons(1)
    server_battle = ServerBattle(server_poke)
    server_battle.start()


elif argv[1] == "-o":
    #offline
    pass
elif argv[1] == "-c":
    #cliente
    pass
else:
    print("Sevidor: -s\nCliente: -c\nOffline: -o")
poke1, poke2 = pokereader.read_pokemons()
battle = Battle(poke1, poke2)
battle.run_battle()
