import sys
from Battle import Battle
from PokeReader import PokeReader

pokereader = PokeReader()
poke1, poke2 = pokereader.read_pokemons()
battle = Battle(poke1, poke2)
battle.run_battle()


