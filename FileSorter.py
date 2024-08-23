import os as myOS

#Directory with stuff to be sorted
unsorted_file_directory = str(r"c:\Users\Yan\Documents\codingExercises\FileSorter-1\Testfolder")
#Path where sorted folders will go
sorted_directory = str(r"c:\Users\Yan\Documents\codingExercises\FileSorter-1\Testfolder\sortedFolders")
counter_moved_files = 0

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
    global counter_moved_files
    createfoldersforgivenextensions(origin_directory, destination_directory)
    for file in myOS.listdir(origin_directory):
        filename, fileextension = myOS.path.splitext(file)
        if fileextension != "":
            print("Origin: " + origin_directory + "\\" + file)
            print("Destination: " + destination_directory + "\\" + fileextension + "\\" + file)
            myOS.rename(origin_directory + "\\" + file, destination_directory + "\\" + fileextension + "\\" + file)
            counter_moved_files = counter_moved_files + 1

sortfilestofolders(unsorted_file_directory, sorted_directory)
print("Moved files: " + str(counter_moved_files))