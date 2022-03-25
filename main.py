# ---------- Packages -----------

from pdf2docx import parse
import os
from os.path import isfile, join

# ------------ Start Execution -------------

# Folder path
path = os.getcwd() + r"\pdf2docx-files"


# Adding all available files in a list
all_files = [ f for f in os.listdir(path) if isfile(join(path, f))]

# Converting
for i in all_files:
    if i[-4:]=='.pdf':
        parse(path+"\\"+i)
print("All files have been converted")
