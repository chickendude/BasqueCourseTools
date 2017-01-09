# BasqueCourseTools
Some Python tools to help process a subtitle corpus and create a language course.

Note that these tools expect your files to be encoded in UTF-8.

## Usage
* `--strip-subtitles` creates a series of files with all subtitle data removed, only sentences left.
* `--combine-corpus` combines all sentence .txt files into one corpus file.
* `--create-frequency` uses the corpus .txt file to create a frequency list.

## strip_subs.py
*requires [pysrt](https://github.com/byroot/pysrt)*  
Pass it a list of filenames and it will extract the sentences and attempt to clean bad conversions to utf-8.

## corpus_funcs.py
A set of functions for building and analyzing the corpus.

#### combineSentences(dir)
Pass it a directory and it will combine all .txt files into one corpus.txt file.

#### createFrequencyDict()
Uses `corpus.txt` to create a frequency list.