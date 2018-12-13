from os import listdir
from os.path import isfile, join

for files in listdir("/home/xhexe"):
    if isfile(join("/home/xhexe", files)):
        print(files)
