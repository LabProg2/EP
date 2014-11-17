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
parser.add_argument("-@", "--at", help="The address of the server", type=str)
args = parser.parse_args()

if not args.at:
    args.at = 'localhost:5000'

server_info = args.at.split(':')
address = server_info[0]
if len(server_info) < 2:
    port = 5000
port = server_info[1]

pokereader = PokeReader()
if args.server:
    server_poke = pokereader.read_pokemons(1)
    server_battle = ServerBattle(server_poke, host=address, port=port)
    server_battle.start(muted = False)

elif args.client:
    client_poke = pokereader.read_pokemons(1)
    client_battle = ClientBattle(client_poke, server_address="http://" + address, server_port=port)
    client_battle.run_battle()

elif args.offline:
    poke1, poke2 = pokereader.read_pokemons(2)
    offline_battle = OfflineBattle(poke1, poke2)
    offline_battle.run_battle()

else:
    parser.print_help()
