

import shutil
import os

""" Short script that copy files from one directory to another."""

mov_files = os.listdir()
""" list of files of the current directory. """

def movFiles():
    """ Function to print the working directory print the files of the directory. """
   
    print(os.getcwd())
    """ Print the current directory """
    
    print(mov_files)
    """ Printing the files, yet again """



def checkDir():
   """ Function to check if directory exist before creating a new directory. """
   
   if os.path.isdir('/Users/haji/Desktop/video_clips'):
       """ Check if 'video clips' directory exist. """
       
       print("Directory Already Exist!")
       
       
   else:
       os.makedirs('/Users/haji/Desktop/video_clips')
       """ Create a directory. """
       
       print('Directory is created.')
       



def CopyMovFiles():
    """ Function to copy files that ends with '.mov' """
   
    for files in mov_files:
        """ Loops through all the files"""
        
        if files.endswith('.mov'):
          """ Look for files that endswith '.mov' """

          shutil.copy(files, '/Users/haji/Desktop/video_clips')
          """Copy them to 'video_clips' directory"""
          
          print(files)
          """ Print files that endswith .mov """


# Run all the function under one function. 
def run():
  movFiles()
  checkDir()
  CopyMovFiles()
run()


       
