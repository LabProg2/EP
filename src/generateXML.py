from lxml import etree
from src.Pokemon import Pokemon
from src.Stats import Stats
from src.Type import Type
from src.Move import Move
from src.movelist import MoveList


class generateXML:
    '''
	Class that receives a pokemon and returns a string with xml format
	'''

    def __init__(self, pokemon):
        ''' Class constructor
			@param pokemon pokemon that will be used to create the xml
		'''

        # Creating the elements:

        xml = etree.Element("battle_state")

        pokemonElm = etree.SubElement(xml, "pokemon")

        nameElm = etree.SubElement(pokemonElm, "name")
        levelElm = etree.SubElement(pokemonElm, "level")
        attributesElm = etree.SubElement(pokemonElm, "attributes")

        healthElm = etree.SubElement(attributesElm, "health")
        attackElm = etree.SubElement(attributesElm, "attack")
        defenseElm = etree.SubElement(attributesElm, "defense")
        speedElm = etree.SubElement(attributesElm, "speed")
        specialElm = etree.SubElement(attributesElm, "special")

        typeElm = etree.SubElement(pokemonElm, "type")
        typeElm2 = etree.SubElement(pokemonElm, "type")

        # Putting the pokemon attributes inside the elements:

        nameElm.text = str(pokemon.name)
        levelElm.text = str(pokemon.level)

        healthElm.text = str(pokemon.hp)
        attackElm.text = str(pokemon.attack)
        defenseElm.text = str(pokemon.defense)
        speedElm.text = str(pokemon.speed)
        specialElm.text = str(pokemon.special)

        typeElm.text = str(pokemon.type_list(0))
        typeElm2.text = str(pokemon.type_list(1))

        # Creating the attacks/moves elements and inserting the attack/moves:

        attacksElm = etree.SubElement(pokemonElm, "attacks")

        attackidElm = etree.SubElement(attacksElm, "id")
        attackidElm.text = "1"

        attacknameElm = etree.SubElement(attacksElm, "name")
        attacknameElm.text = pokemon.moves.get_move(0).name

        attacktypeElm = etree.SubElement(attacksElm, "type")
        attacktypeElm.text = str(pokemon.moves.get_move(0).elm_type)

        attackpowerElm = etree.SubElement(attacksElm, "power")
        attackpowerElm.text = str(pokemon.moves.get_move(0).power)

        attackaccuracyElm = etree.SubElement(attacksElm, "accuracy")
        attackaccuracyElm.text = str(pokemon.moves.get_move(0).accuracy)

        attackpowerpointsElm = etree.SubElement(attacksElm, "power_points")
        attackpowerpointsElm.text = str(pokemon.moves.get_move(0).pp)

        # Pokemons has many moves (probably there is a better way to do this)

        if len(pokemon.moves) > 2:
            attacksElm2 = etree.SubElement(pokemonElm, "attacks")

            attackidElm2 = etree.SubElement(attacksElm2, "id")
            attackidElm2.text = "2"

            attacknameElm2 = etree.SubElement(attacksElm2, "name")
            attacknameElm2.text = pokemon.moves.get_move(1).name

            attacktypeElm2 = etree.SubElement(attacksElm2, "type")
            attacktypeElm2.text = str(pokemon.moves.get_move(1).elm_type)

            attackpowerElm2 = etree.SubElement(attacksElm2, "power")
            attackpowerElm2.text = str(pokemon.moves.get_move(1).power)

            attackaccuracyElm2 = etree.SubElement(attacksElm2, "accuracy")
            attackaccuracyElm2.text = str(pokemon.moves.get_move(1).accuracy)

            attackpowerpointsElm2 = etree.SubElement(attacksElm2, "power_points")
            attackpowerpointsElm2.text = str(pokemon.moves.get_move(1).pp)

        if len(pokemon.moves) > 3:
            attacksElm3 = etree.SubElement(pokemonElm, "attacks")

            attackidElm3 = etree.SubElement(attacksElm3, "id")
            attackidElm3.text = "3"

            attacknameElm3 = etree.SubElement(attacksElm3, "name")
            attacknameElm3.text = pokemon.moves.get_move(2).name

            attacktypeElm3 = etree.SubElement(attacksElm3, "type")
            attacktypeElm3.text = str(pokemon.moves.get_move(2).elm_type)

            attackpowerElm3 = etree.SubElement(attacksElm3, "power")
            attackpowerElm3.text = str(pokemon.moves.get_move(2).power)

            attackaccuracyElm3 = etree.SubElement(attacksElm3, "accuracy")
            attackaccuracyElm3.text = str(pokemon.moves.get_move(2).accuracy)

            attackpowerpointsElm3 = etree.SubElement(attacksElm3, "power_points")
            attackpowerpointsElm3.text = str(pokemon.moves.get_move(2).pp)

        if len(pokemon.moves) > 4:
            attacksElm4 = etree.SubElement(pokemonElm, "attacks")

            attackidElm4 = etree.SubElement(attacksElm4, "id")
            attackidElm4.text = "4"

            attacknameElm4 = etree.SubElement(attacksElm4, "name")
            attacknameElm4.text = pokemon.moves.get_move(4).name

            attacktypeElm4 = etree.SubElement(attacksElm4, "type")
            attacktypeElm4.text = str(pokemon.moves.get_move(4).elm_type)

            attackpowerElm4 = etree.SubElement(attacksElm4, "power")
            attackpowerElm4.text = str(pokemon.moves.get_move(4).power)

            attackaccuracyElm4 = etree.SubElement(attacksElm4, "accuracy")
            attackaccuracyElm4.text = str(pokemon.moves.get_move(4).accuracy)

            attackpowerpointsElm4 = etree.SubElement(attacksElm4, "power_points")
            attackpowerpointsElm4.text = str(pokemon.moves.get_move(4).pp)

        return (etree.tostring(xml, xml_declaration = True, pretty_print = True, encoding="UTF-8"))


pokemon = Pokemon(Type.Normal.value, Stats(100,100,100,100,100), MoveList(Move("move1",Type.Normal.value,3,2,1)))
xml = generateXML(pokemon)
print(xml)