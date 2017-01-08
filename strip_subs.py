import pysrt
import os
import re

black_list = ['Euskal Encodings','azpitituluak','euskarazko','fharlock','arkadia','euskal','Jon Mu','AKETek','\u266b',"YIFY","euskaratz","Team Nanban","Ghibli"]
output_folder = "out"

def pullSentences(filelist):
	os.makedirs(output_folder, exist_ok=True)
	i = 0
	for filename in filelist:
		i += 1
		print("File " + str(i) + " " + filename)
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
									.replace("â€œ","\"")\
									.replace("â€","\"")\
									.replace("Â","")\
									.replace("\u266a","")\
									.replace("\x8f","è")\
									.replace("Ã\x81","Á")\
									.replace("\u014d","o")\
									.replace("\ufffd","ñ")\
									.replace("\r\n","\n")\
									.replace("\n"," ") + "\n"
		print(subtitle_text)
		print(filename)
		filename = str(i) + ".txt"
		file_path = os.path.join(output_folder,filename)
		with open(file_path, 'w') as f:
			f.write(subtitle_text)
