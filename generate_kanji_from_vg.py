from xml.etree import ElementTree as ET



def kanjivg_xml_to_image(tag, strokes):
	"""
	Recursively traverses the given `tag` and appends all found strokes
	to the `strokes` list.

	Note: This function works in-place and adds all found elements to the `strokes`-list

	Args:
		tag       (str) : 
		strokes ([str]) : A nested list containing all strokes.

	"""

	# this is a radical (consists of multipe strokes) of the kanji
	if(tag.tag == 'g'):
		# iterate over all children of the radical
		for child in tag:
			# if the child of this radical is another radical
			# add a list to store all strokes belonging to this radical in
			if(child.tag == 'g'):
				path = []
				strokes.append(path)
				kanjivg_xml_to_image(child, path)
			# if it is a leave than don't add a new list but add the indivdual strokes
			else:
				kanjivg_xml_to_image(child, strokes)
	# this is a stroke
	elif(tag.tag == 'path'):
		strokes.append(tag.attrib['d'])


def strokes_to_image(strokes):
	pass

if __name__ == "__main__":

	# read the kanjivg data base from file
	tree = ET.parse('kanjivg.xml')
	root = tree.getroot()

	# read all jis level 2 characters from file
	kanjis = None
	with open(r"E:\projects\DaKanjiRecognizerML\single_kanji_cnn\jis2_characters.txt", encoding="utf8") as f:
		kanji = f.read()
	kanjis = kanji.replace("\n", " ").split(" ")

	# iterate over all kanji xml tags
	cnt = 0
	for child in root:

		hex = child.attrib['id'].removeprefix("kvg:kanji_")
		kanji = chr(int(hex, 16))
		if(kanji == '晰'):
			strokes = []
			kanjivg_xml_to_image(child[0], strokes)
			print(strokes)

	print(cnt)
