import sys,os
import sqlite3
from glob import glob

import strip_subs
import corpus_funcs

# make sure all files are utf-8!
# files ready to be extracted should be placed in the 'subtitles' folder
subtitles_dir = "subtitles"
def main():

	# command line options
	if len(sys.argv) > 1:
		args = sys.argv[1:]
		if "--strip-subtitles" in args:
			path = os.path.join(subtitles_dir, "*.srt")
			filelist = glob(path)
			strip_subs.pullSentences(filelist)
		if "--create-frequency" in args:
			corpus_funcs.createFrequencyDict()
		if "--combine-corpus" in args:
			corpus_funcs.combineSentences("out")
		if "--build-corpus" in args:
			corpus_funcs.buildCorpus()


if __name__ == '__main__':
	main()
# # connect to db
# connection = sqlite3.connect('database.db')
# cursor = connection.cursor()
#
# # create table
# sql = "CREATE TABLE SentenceGroup \
#    (id INTEGER PRIMARY KEY AUTOINCREMENT, \
#    title TEXT, \
#    score INTEGER)"
#
# # cursor.execute(sql)
#
# sql = "INSERT INTO SentenceGroup (title, score) VALUES ('sentences', 1)"
# cursor.execute(sql)
#
# cursor.execute("SELECT * FROM SentenceGroup")
# for records in cursor.fetchall():
# 	print(records)
#
# connection.commit()
# connection.close()
