from sys import stdin
from lxml import etree
from lxml import objectify

class generateXML:
	'''
	description
	'''

	def __init__(self,File):

		inputFile = open(File,"r")
		stringFile = inputFile.read()

		splitedString = stringFile.split('\n')

		name = splitedString[0]
		level = splitedString[1]

		health = splitedString[2]
		attack = splitedString[3]
		defense = splitedString[4]
		speed = splitedString[5]
		special = splitedString[6]

		type = splitedString[7]
		type2 = splitedString[8]

		numattacks = splitedString[9]

		attackid = '1'
		attackname = splitedString[10]
		attacktype = splitedString[11]
		attackpower = splitedString[12]
		attackaccuracy = splitedString[13]
		attackpowerpoints = splitedString[14]

		if splitedString[9] >= '2':
			attackid2 = '2'
			attackname2 = splitedString[15]
			attacktype2 = splitedString[16]
			attackpower2 = splitedString[17]
			attackaccuracy2 = splitedString[18]
			attackpowerpoints2 = splitedString[19]

		if splitedString[9] >= '3':
			attackid3 = '3'
			attackname3 = splitedString[20]
			attacktype3 = splitedString[21]
			attackpower3 = splitedString[22]
			attackaccuracy3 = splitedString[23]
			attackpowerpoints3 = splitedString[24]

		if splitedString[9] >= '4':
			attackid4 = '4'
			attackname4 = splitedString[25]
			attacktype4 = splitedString[26]
			attackpower4 = splitedString[27]
			attackaccuracy4 = splitedString[28]
			attackpowerpoints4 = splitedString[29]

		if splitedString[9] >= '5':
			attackid5 = '5'
			attackname5 = splitedString[30]
			attacktype5 = splitedString[31]
			attackpower5 = splitedString[32]
			attackaccuracy5 = splitedString[33]
			attackpowerpoints5 = splitedString[34]		

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
		typeElm2 = etree.SubElement(pokemonElm,"type")

		attacksElm = etree.SubElement(pokemonElm,"attacks")

		attackidElm = etree.SubElement(attacksElm,"id")
		attacknameElm = etree.SubElement(attacksElm,"name")
		attacktypeElm = etree.SubElement(attacksElm,"type")
		attackpowerElm = etree.SubElement(attacksElm,"power")
		attackaccuracyElm = etree.SubElement(attacksElm,"accuracy")
		attackpowerpointsElm = etree.SubElement(attacksElm,"power_points")

		if splitedString[9] >= '2':
			attacksElm2 = etree.SubElement(pokemonElm,"attacks")
			attackidElm2 = etree.SubElement(attacksElm2,"id")
			attacknameElm2 = etree.SubElement(attacksElm2,"name")
			attacktypeElm2 = etree.SubElement(attacksElm2,"type")
			attackpowerElm2 = etree.SubElement(attacksElm2,"power")
			attackaccuracyElm2 = etree.SubElement(attacksElm2,"accuracy")
			attackpowerpointsElm2 = etree.SubElement(attacksElm2,"power_points")

		if splitedString[9] >= '3':
			attacksElm3 = etree.SubElement(pokemonElm,"attacks")
			attackidElm3 = etree.SubElement(attacksElm3,"id")
			attacknameElm3 = etree.SubElement(attacksElm3,"name")
			attacktypeElm3 = etree.SubElement(attacksElm3,"type")
			attackpowerElm3 = etree.SubElement(attacksElm3,"power")
			attackaccuracyElm3 = etree.SubElement(attacksElm3,"accuracy")
			attackpowerpointsElm3 = etree.SubElement(attacksElm3,"power_points")

		if splitedString[9] >= '4':
			attacksElm4 = etree.SubElement(pokemonElm,"attacks")
			attackidElm4 = etree.SubElement(attacksElm4,"id")
			attacknameElm4 = etree.SubElement(attacksElm4,"name")
			attacktypeElm4 = etree.SubElement(attacksElm4,"type")
			attackpowerElm4 = etree.SubElement(attacksElm4,"power")
			attackaccuracyElm4 = etree.SubElement(attacksElm4,"accuracy")
			attackpowerpointsElm4 = etree.SubElement(attacksElm4,"power_points")

		if splitedString[9] >= '5':
			attacksElm5 = etree.SubElement(pokemonElm,"attacks")
			attackidElm5 = etree.SubElement(attacksElm5,"id")
			attacknameElm5 = etree.SubElement(attacksElm5,"name")
			attacktypeElm5 = etree.SubElement(attacksElm5,"type")
			attackpowerElm5 = etree.SubElement(attacksElm5,"power")
			attackaccuracyElm5 = etree.SubElement(attacksElm5,"accuracy")
			attackpowerpointsElm5 = etree.SubElement(attacksElm5,"power_points")	

		nameElm.text = name
		levelElm.text = level

		healthElm.text = health
		attackElm.text = attack
		defenseElm.text = defense
		speedElm.text = speed
		specialElm.text = special

		typeElm.text = type
		typeElm2.text = type2

		attackidElm.text = attackid
		attacknameElm.text = attackname
		attacktypeElm.text = attacktype
		attackpowerElm.text = attackpower
		attackaccuracyElm.text = attackaccuracy
		attackpowerpointsElm.text = attackpowerpoints

		if splitedString[9] >= '2':
			attackidElm2.text = attackid2
			attacknameElm2.text = attackname2
			attacktypeElm2.text = attacktype2
			attackpowerElm2.text = attackpower2
			attackaccuracyElm2.text = attackaccuracy2
			attackpowerpointsElm2.text = attackpowerpoints2

		if splitedString[9] >= '3':
			attackidElm3.text = attackid3
			attacknameElm3.text = attackname3
			attacktypeElm3.text = attacktype3
			attackpowerElm3.text = attackpower3
			attackaccuracyElm3.text = attackaccuracy3
			attackpowerpointsElm3.text = attackpowerpoints3

		if splitedString[9] >= '4':
			attackidElm4.text = attackid4
			attacknameElm4.text = attackname4
			attacktypeElm4.text = attacktype4
			attackpowerElm4.text = attackpower4
			attackaccuracyElm4.text = attackaccuracy4
			attackpowerpointsElm4.text = attackpowerpoints4

		if splitedString[9] >= '5':
			attackidElm5.text = attackid5
			attacknameElm5.text = attackname5
			attacktypeElm5.text = attacktype5
			attackpowerElm5.text = attackpower5
			attackaccuracyElm5.text = attackaccuracy5
			attackpowerpointsElm5.text = attackpowerpoints5

		return(etree.tostring(corpo, xml_declaration=True, pretty_print = True, encoding="UTF-8"))