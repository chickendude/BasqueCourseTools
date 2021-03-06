# -- coding: utf-8 --
import pysrt
import os,glob
import re


black_list = ['Euskal Encodings','azpitituluak','euskaraz','.com','://','@','fharlock','arkadia','euskal','Jon Mu','AKETek','\u266b',"YIFY","euskaratz","Team Nanban","Ghibli"]
output_folder = "out"

def pullSentences(filelist):
	os.makedirs(output_folder, exist_ok=True)
	i = 0
	for filename in filelist:
		i += 1
		print("Processing: " + str(i) + " " + filename)
		subtitle = pysrt.open(filename)
		subtitle_text = ""
		for line in subtitle:
			text = str(line.text)
			p = re.compile(r'<.*?>')
			text = p.sub('', text)
			if not any(x.lower() in text.lower() for x in black_list):
				subtitle_text += text\
									.replace("â€¦","...")\
									.replace('Ã±','ñ')\
									.replace("\x9d","")\
									.replace("â™ª","")\
									.replace("Ã©","é")\
									.replace("\x8f","è")\
									.replace("Ã‰","É")\
									.replace("Ãˆ","È")\
									.replace("Ã\x81","Á")\
									.replace("\u014d","o")\
									.replace("\ufffd","ñ")\
									.replace("â€œ","\"")\
									.replace("â€","\"")\
									.replace("Â","")\
									.replace("\u266a","")\
									.replace("\r\n","\n")\
									.replace("\n"," ") + "\n"
		filename = str(i) + ".txt"
		file_path = os.path.join(output_folder,filename)
		with open(file_path, 'w') as f:
			f.write(subtitle_text)
