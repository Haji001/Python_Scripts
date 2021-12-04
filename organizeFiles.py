import os
import shutil as sh

dir_path = os.path.dirname(os.path.realpath(__file__))
print(dir_path)

list = os.listdir(dir_path)
print(list)

for filename in list:
    if filename.startswith("c"):
        if not os.path.exists('effiles'):
            os.mkdir('effiles')
        sh.copy(filename, "effiles")

if filename.startswith("f"):
    sh.copy(filename, "effiles")

if not os.path.exists("bashing_file.py"):
    open("bashing_file.py", 'w').close()

print("Finish organizing foles")