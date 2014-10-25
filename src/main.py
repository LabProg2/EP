import sys
from Pokemon import Pokemon
from Stats import Stats
from Move import Move
from Type import Type

def createPoke(poke_file):
    name = poke_file.readline()
    lvl = poke_file.readline()
    hp = poke_file.readline()
    atk = poke_file.readline()
    defe = poke_file.readline()
    spd = poke_file.readline()
    spc = poke_file.readline()
    tp = int(poke_file.readline())
    typ1 = Type(tp)
    tp = int(poke_file.readline())
    typ2 = Type(tp)
    typ_list = typ1, typ2
    nat = poke_file.readline()
    print("stats: " + name + str(lvl) + str(hp) + str(atk) + str(defe) + str(spd) + str(spc) + str(typ1) + str(typ2) + str(nat))
    stats = Stats(hp, atk, defe, spd, spc)
    print(stats)
    move_list = []
    for i in range(int(nat)):
        move_name = poke_file.readline()
        move_type = poke_file.readline()
        move_acu = poke_file.readline()
        move_pwr = poke_file.readline()
        move_pp = poke_file.readline()
        move = Move(move_name, move_type, move_acu, move_pwr, move_pp)
        print("moooove, beeach: " + move_name + move_type + move_acu + move_pwr + move_pp)
        print(move)
        move_list.append(move)
    return Pokemon(typ_list, stats, name, level, move_list)

try:
    poke1_path = sys.argv[1]
except IndexError:
    print("Por favor, entre com o caminho do arquivo com o primeiro pokemon")

try:
    poke2_path = sys.argv[2]
except IndexError:
    print("Por favor, entre com o caminho do arquivo com o segundo pokemon")

try:
    poke1_f = open(poke1_path, 'r')
except FileNotFoundError:
    print("Não foi possivel abrir o arquivo do primeiro pokemon")

try:
    poke2_f = open(poke2_path, 'r')
except FileNotFoundError:
    print("Não foi possivel abrir o arquivo do segundo pokemon")

poke1 = createPoke(poke1_f)
poke2 = createPoke(poke2_f)


