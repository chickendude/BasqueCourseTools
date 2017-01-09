# BasqueCourseTools
Some Python tools to help process a subtitle corpus and create a language course.

Note that these tools expect your files to be encoded in UTF-8.

## strip_subs
*requires [pysrt](https://github.com/byroot/pysrt)*  
Pass it a list of filenames and it will extract the sentences and attempt to clean bad conversions to utf-8.

### Usage
`python course_tools --strip-subtitles`