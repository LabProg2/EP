import sys
from ServerBattle import ServerBattle
from OfflineBattle import OfflineBattle
from PokeReader import PokeReader
from sys import argv

pokereader = PokeReader()
if argv[1] == "-s":
    server_poke = pokereader.read_pokemons(1)
    server_battle = ServerBattle(server_poke)
    server_battle.start(debugging = True)


elif argv[1] == "-o":
    poke1, poke2 = pokereader.read_pokemons(2)
    offline_battle = OfflineBattle(poke1, poke2)
    offline_battle.run_battle()

elif argv[1] == "-c":
    client_poke = pokereader.read_pokemons(1)
    client_battle = ClientBattle(client_poke)
    pass
else:
    print("Sevidor: -s\nCliente: -c\nOffline: -o")