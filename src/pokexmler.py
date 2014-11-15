from xml.etree.ElementTree import Element, SubElement, tostring, fromstring
from xml.dom import minidom 

class PokeXmler:
    '''
	Class that receives a pokemon and returns a string with xml format
	'''

    def __init__(self, *pokemons):
        ''' Class constructor
			@param pokemon pokemon that will be used to create the xml
		'''

        # Creating the elements:

        xml = Element("battle_state")

        for pokemon in pokemons:
            pokemonElm = SubElement(xml, "pokemon")

            nameElm = SubElement(pokemonElm, "name")
            nameElm.text = pokemon.name
            
            levelElm = SubElement(pokemonElm, "level")
            levelElm.text = str(pokemon.level)
            
            attributesElm = SubElement(pokemonElm, "attributes")

            healthElm = SubElement(attributesElm, "health")
            healthElm.text = str(pokemon.hp)

            attackElm = SubElement(attributesElm, "attack")
            attackElm.text = str(pokemon.attack)

            defenseElm = SubElement(attributesElm, "defense")
            defenseElm.text = str(pokemon.defense)

            speedElm = SubElement(attributesElm, "speed")
            speedElm.text = str(pokemon.speed)

            specialElm = SubElement(attributesElm, "special")
            specialElm.text = str(pokemon.special)

            typeElm = SubElement(pokemonElm, "type")
            typeElm.text = str(pokemon.type_list[0].value)

            typeElm2 = SubElement(pokemonElm, "type")
            typeElm2.text = str(pokemon.type_list[1].value)

            # Creating the attacks/moves elements and inserting the attack/moves:

            for i, move in enumerate(pokemon.moves):
                attacksElm = SubElement(pokemonElm, "attacks")

                attackidElm = SubElement(attacksElm, "id")
                attackidElm.text = str(i)

                attacknameElm = SubElement(attacksElm, "name")
                attacknameElm.text = move.name

                attacktypeElm = SubElement(attacksElm, "type")
                attacktypeElm.text = str(move.elm_type.value)

                attackpowerElm = SubElement(attacksElm, "power")
                attackpowerElm.text = str(move.power)

                attackaccuracyElm = SubElement(attacksElm, "accuracy")
                attackaccuracyElm.text = str(move.accuracy)

                attackpowerpointsElm = SubElement(attacksElm, "power_points")
                attackpowerpointsElm.text = str(move.pp)

        self._tree = xml

    @property
    def tree(self):
        return self._tree
    
    def tostring(self):
        xmlstr = tostring(self._tree, encoding="UTF-8")
        xmlstr = minidom.parseString(xmlstr)
        return xmlstr.toprettyxml(indent="\t")

    def string_to_xml(self, string):
        return fromstring(string)

