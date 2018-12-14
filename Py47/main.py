import os, glob

files = glob.glob("*/home/xhexe/Dokumenty/*.txt")
files.sort(key = os.path.getmtime)

print("\n".join(files))