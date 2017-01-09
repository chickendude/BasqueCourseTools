import os, glob


def combineSentences(dir):
	dir = os.path.join(dir, "*.txt")
	file_list = glob.glob(dir)
	with open("corpus.txt", "w") as corpus:
		for file in file_list:
			subtitle = ""
			with open(file, "r") as f:
				subtitle += f.read()
			corpus.write(subtitle)


def createFrequencyDict():
	return None


def buildCorpus():
	return None