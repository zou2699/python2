#!/usr/bin/env python
# encoding: utf-8
# encoding: utf-8



import difflib
import sys
try:
    textfile1=sys.argv[1]
    textfile2=sys.argv[2]
except Exception, e:
    print "Error: " + str(e)
    print "Usage: diff.py filename1 filename2"
    sys.exit()

def readfile (filename):  #文件读取分割函数
    try:
        fileHandle = open (filename, 'rb')
        text = fileHandle.read().splitlines() #读取后进行分行处理
        fileHandle.close()
        return text
    except IOError as error:
        print ('Read file Error: ' + str(error) )
        sys.exit()

if textfile1 == "" or textfile2 == "":
    print "Usage: diff.py filename1 filename2"
    sys.exit()
text1_lines = readfile(textfile1)  #调用readfile函数
text2_lines = readfile(textfile2)
d = difflib.HtmlDiff()
print d.make_file(text1_lines, text2_lines)
