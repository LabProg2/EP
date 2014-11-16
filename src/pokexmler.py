from xml.etree.ElementTree import Element, SubElement, tostring, fromstring
from xml.dom import minidom 
from Pokemon import Pokemon
from Stats import Stats
from Type import Type
from Move import Move
from movelist import MoveList
from re import sub

class PokeXmler:
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
        try:
            xml = str(xml)
        except:
            raise TypeError("The xml must be a string")


        xml = self._clean_xml(xml)
        battle_state = fromstring(xml)

        pokemons = []
        for poke in battle_state:
            name = poke.find('name').text
            level = poke.find('level').text
            types = []
            for typ in poke.findall('type'):
                types.append(Type(int(typ.text)))   
            attributes = poke.find('attributes')
            hp = attributes.find('health').text
            attack = attributes.find('attack').text
            defense = attributes.find('defense').text
            speed = attributes.find('speed').text
            special = attributes.find('special').text
            moves = []
            for move in poke.findall('attacks'):
                move_name = move.find('name').text
                move_power = move.find('power').text
                move_accuracy = move.find('accuracy').text
                move_pp = move.find('power_points').text
                move_id = int(move.find('id').text)
                move_type = Type(int(move.find('type').text))
                new_move = Move(name=move_name, elm_type=move_type, accuracy=move_accuracy, \
                     power=move_power, pp=move_pp)
                moves.insert(move_id, new_move)
            moves = MoveList(moves)
            stats = Stats(hp=hp, attack=attack, defense=defense, speed=speed, special=special)
            pokemon = Pokemon(name=name, level=level, stats=stats, type_list=types, moves=moves)
            pokemons.append(pokemon)
        return pokemons

    def _clean_xml(self, xml):
        xml = sub(r'\\n|\\t|b\'', '', xml)
        xml = sub(r'(<\?.*\?>)', '', xml)
        xml = sub(r'\'', '', xml)
        return xml
