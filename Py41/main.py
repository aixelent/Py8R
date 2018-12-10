import os

print(int(os.popen("ls | wc -l").read()))