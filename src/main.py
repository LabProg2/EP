import sys
from ServerBattle import ServerBattle
from OfflineBattle import OfflineBattle
from ClientBattle import ClientBattle
from PokeReader import PokeReader
from sys import argv
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-s", "--server", help="Server mode", action="store_true")
parser.add_argument("-c", "--client", help="Client mode", action="store_true")
parser.add_argument("-o", "--offline", help="Offline mode", action="store_true")
args = parser.parse_args()

pokereader = PokeReader()
if args.server:
    server_poke = pokereader.read_pokemons(1)
    server_battle = ServerBattle(server_poke)
    server_battle.start(muted = False)

elif args.client:
    client_poke = pokereader.read_pokemons(1)
    client_battle = ClientBattle(client_poke)
    client_battle.run_battle()

elif args.offline:
    poke1, poke2 = pokereader.read_pokemons(2)
    offline_battle = OfflineBattle(poke1, poke2)
    offline_battle.run_battle()

else:
    parser.print_help()
