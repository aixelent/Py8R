import os

print([files for files in os.listdir("/home/xhexe/Py/Py8R") if os.path.isfile(os.path.join("/home/xhexe/Py/Py8R", files))])
