import sys
from Battle import Battle

try:
    poke1_path = sys.argv[1]
except IndexError:
    print("Please, enter the first pokemon file path")

try:
    poke2_path = sys.argv[2]
except IndexError:
    print("Please, enter the second pokemon file path")

battle = Battle(poke1_path, poke2_path)
battle.run_battle()


