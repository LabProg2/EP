from xml.etree.ElementTree import Element, SubElement, tostring, fromstring
from xml.dom import minidom 
from lxml import objectify

class pokexmler:
    '''
	This class is used to transform xml to pokemons and pokemons to xml
	'''
    def __init__(self):
        self._tree = None

    def pokes_to_xml(self, *pokemons):
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
        return self.tostring()

    @property
    def tree(self):
        return self._tree
    
    def tostring(self):
        try:
            xmlstr = tostring(self._tree, encoding="UTF-8")
            xmlstr = minidom.parseString(xmlstr)
        except:
            raise RuntimeError("It wasn't possible to produce a string from the xml")
        return xmlstr.toprettyxml(indent="\t")

    def str_to_pokes(self, xml):
        '''This class receives a string and returns a list of pokemons representing the pokemons of the xml
        :param xml: the string with the xml info
        '''
        x = fromstring(xml)
        main = objectify.x
        numberofpokemons = str(xml).count('<pokemon>')
        auxiliar_listofpokemons = str(xml).split('<pokemon>') # used to count the number of attacks of ONE pokemon

        for i in range(1, numberofpokemons):
            name = main.pokemon[i].name
            level = main.pokemon[i].level

            if str(auxiliar_listofpokemons[i].count('<type>')) == 1:
                type_list = Type(main.pokemon[i].type)
            else:
                type_list[1] = Type(main.pokemon[i].type[1])
                type_list[2] = Type(main.pokemon[i].type[2])

            hp = main.pokemon[i].attributes.health
            attack = main.pokemon[i].attributes.attack
            defense = main.pokemon[i].attributes.defense
            speed = main.pokemon[i].attributes.speed
            special = main.pokemon[i].attributes.special
            stats = Stats(hp, attack, defense, speed, special)

            numberofattacks = str(auxiliar_listofpokemons[i]).count('<attacks>')
            for j in range(1, numberofattacks):
                attackname = main.pokemon[i].attacks[j].name
                attacktype = Type(main.pokemon[i].attacks[j].type)
                attackpower = main.pokemon[i].attacks[j].power
                attackaccuracy = main.pokemon[i].attacks[j].accuracy
                attackpowerpoints = main.pokemon[i].attacks[j].power_points
                MoveList[j] = Move(attackname, attacktype, attackpower, attackaccuracy, attackpowerpoints)

            listofpokemons[i] = Pokemon(type_list, stats, MoveList, name, level)
        return(listofpokemons)    
