import os 
import shutil


"""Create a program that scans a specified directory and organizes 
the files into different folders based on their file extensions."""

def OrganizingFiles(targetDirectory): 

    exTensions = {'txt': 'TextFiles',
                  'jpg': 'JpgFiles',
                  'png': 'PngFiles'}
    

    for filename in os.listdir(targetDirectory):

        if os.path.isfile(os.path.join(targetDirectory, filename)):
            fileExtension = filename.split('.')[-1].lower()
           
            if fileExtension in exTensions:
                folderName = exTensions[fileExtension]
                folderPath = os.path.join(targetDirectory, folderName)

            if not os.path.exists(folderPath):
                os.mkdir(folderPath)

            source = os.path.join(targetDirectory, filename)
            destination = os.path.join(folderPath, filename)
            shutil.move(source, destination)



    print("Files moved successfully.")

OrganizingFiles(targetDirectory='/path/file')