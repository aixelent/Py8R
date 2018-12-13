import os
import csv

path_write_csv = "/home/xhexe/Py/Py8R/files"

with open(os.path.join(path_write_csv, "discogs.csv"), "w") as my_movies:
    file_writer = csv.writer(my_movies)
    file_writer.writerow(["Author", "Rating"])
    file_writer.writerow(["Rebel Without a Cause", 3])
    file_writer.writerow(["Monty Python's Life of Brian", 5])