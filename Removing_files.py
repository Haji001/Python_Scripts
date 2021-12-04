# Remove files with specific extension
import os

# set a object for the file directory
dir = "C:/Users/Hagi/Downloads"


for files in os.listdir(dir):
    if files.endswith(".docx"):
        os.unlink(os.path.join(dir, files))

#   remove files that ends with svg
    if files.endswith(".jpg"):
        os.unlink(os.path.join(dir, files))

        print('files are deleted')
        break




