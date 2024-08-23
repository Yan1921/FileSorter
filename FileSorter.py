import os as myOS

#Directory with stuff to be sorted
unsorted_file_directory = str(r"c:\Users\Yan\Documents\codingExercises\Testfolder")
#Path where sorted folders will go
FolderDirectory = str(r"c:\Users\Yan\Documents\codingExercises\Testfolder\sortedFolders")

def createfoldersforgivenextensions(origin_directory, destination_directory):
    extensions = set(getextensions(origin_directory))
    for extension in extensions:
        newfolder = str(destination_directory + r"\\" + extension)
        if not myOS.path.exists(newfolder):
            myOS.mkdir(newfolder)
            print(extension + "  <-- Folder successfully created!")
        else:
            print(extension + "  <-- Folder already exists!")



def getextensions(directory):
     extensions = []
     for file in myOS.listdir(directory):
        filename, fileextension = myOS.path.splitext(file)
        if fileextension != "":
            extensions.append(fileextension)
     return(extensions)

def sortfilestofolders(origin_directory, destination_directory):
    createfoldersforgivenextensions(origin_directory, destination_directory)
    print("Still working on this one")

createfoldersforgivenextensions(unsorted_file_directory)