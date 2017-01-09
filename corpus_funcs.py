import os, glob
import re
import operator


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
	corpus = glob.glob("corpus.txt")
	if len(corpus) != 1:
		print("Error finding 'corpus.txt'")
		return
	dictionary = {}
	with open(corpus[0], "r") as file:
		i = 0
		for line in file:
			i += 1
			if i % 50000 == 0:
				print(i)
			for word in line.split(" "):
				word = word.strip()
				word = re.sub('[^a-z]', '', word.lower())
				if word == '':
					continue
				if not word in dictionary:
					dictionary[word] = 0
				dictionary[word] += 1
	with open("corpus.csv", "w") as file:
		for word, frequency in sorted(dictionary.items(), key=operator.itemgetter(1), reverse=True):
			file.write("%s\t%s\n" % (word, frequency))


def buildCorpus():
	return None
