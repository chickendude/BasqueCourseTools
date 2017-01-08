import sys
import sqlite3
from glob import glob
from os.path import join

import strip_subs


# make sure all files are utf-8!
# files ready to be extracted should be placed in the 'subtitles' folder
def main():
	path = join("subtitles", "*.srt")
	filelist = glob(path)
	strip_subs.pullSentences(filelist)
	# add in commandline options?
	# if len(sys.argv) > 1:
	# 	args = sys.argv[1:]
	# 	if "..." in args:
	# 		...


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
