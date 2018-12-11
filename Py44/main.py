import os, time

file_path = "/home/xhexe/Py/Py8R/Py999/main.py"

print("File created:", time.ctime(os.path.getctime(file_path)))
print("Last modification time:", time.ctime(os.path.getmtime(file_path)))
print("Last access time:", time.ctime(os.path.getatime(file_path)))
