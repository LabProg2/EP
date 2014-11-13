from lxml import etree
from lxml import objectify

inputFile = open("Alakazam.pok","r")

stringFile = inputFile.read()
print(stringFile)

splitedString = stringFile.split('\n')

name = splitedString[0]
level = splitedString[1]
health = splitedString[2]
attack = splitedString[3]
defense = splitedString[4]
speed = splitedString[5]
special = splitedString[6]
type = splitedString[7]
attackid = splitedString[8]
attackname = splitedString[9]
attacktype = splitedString[10]
attackpower = splitedString[11]
attackaccuracy = splitedString[12]
attackpowerpoints = splitedString[13]

corpo = etree.Element("battle_state")

pokemonElm = etree.SubElement(corpo,"pokemon")

nameElm = etree.SubElement(pokemonElm, "name")
levelElm = etree.SubElement(pokemonElm,"level")
attributesElm = etree.SubElement(pokemonElm,"attributes")

healthElm = etree.SubElement(attributesElm,"health")
attackElm = etree.SubElement(attributesElm,"attack")
defenseElm = etree.SubElement(attributesElm,"defense")
speedElm = etree.SubElement(attributesElm,"speed")
specialElm = etree.SubElement(attributesElm,"special")

typeElm = etree.SubElement(pokemonElm,"type")

attacksElm = etree.SubElement(pokemonElm,"attacks")

attackidElm = etree.SubElement(attacksElm,"id")
attacknameElm = etree.SubElement(attacksElm,"name")
attacktypeElm = etree.SubElement(attacksElm,"type")
attackpowerElm = etree.SubElement(attacksElm,"power")
attackaccuracyElm = etree.SubElement(attacksElm,"accuracy")
attackpowerpointsElm = etree.SubElement(attacksElm,"power_points")

nameElm.text = name
levelElm.text = level

healthElm.text = health
attackElm.text = attack
defenseElm.text = defense
speedElm.text = speed
specialElm.text = special

typeElm.text = type

attackidElm.text = attackid
attacknameElm.text = attackname
attacktypeElm.text = attacktype
attackpowerElm.text = attackpower
attackaccuracyElm.text = attackaccuracy
attackpowerpointsElm.text = attackpowerpoints

print(etree.tostring(corpo, xml_declaration=True, pretty_print = True, encoding="UTF-8"))

outFile = open('teste2.xml','w')
outFile.write(etree.tostring(corpo, xml_declaration=True, pretty_print = True, encoding="UTF-8"))