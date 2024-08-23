import os as myOS

#Directory with stuff to be sorted
unsorted_file_directory = str(r"c:\Users\Yan\Documents\codingExercises\FileSorter-1\Testfolder")
#Path where sorted folders will go
sorted_directory = str(r"c:\Users\Yan\Documents\codingExercises\FileSorter-1\Testfolder\sortedFolders")
counter_folders_created = 0
counter_moved_files = 0

def getextensions(directory):
     extensions = []
     for file in myOS.listdir(directory):
        name_and_extension = myOS.path.splitext(file)
        if name_and_extension[1] != "":
            extensions.append(name_and_extension[1])
     return(extensions)

def create_folders_for_given_extensions(origin_directory, destination_directory):
    global counter_folders_created
    extensions = set(getextensions(origin_directory))
    for extension in extensions:
        newfolder = str(destination_directory + "\\" + extension)
        if not myOS.path.exists(newfolder):
            myOS.mkdir(newfolder)
            print(extension + "  <-- Folder successfully created!")
            counter_folders_created = counter_folders_created + 1
        else:
            print(extension + "  <-- Folder already exists!")

def sort_files_to_folders(origin_directory, destination_directory):
    global counter_moved_files
    create_folders_for_given_extensions(origin_directory, destination_directory)
    for file in myOS.listdir(origin_directory):
        name_and_extension = myOS.path.splitext(file)
        if name_and_extension[1] != "":
            print("Origin: " + origin_directory + "\\" + file)
            print("Destination: " + destination_directory + "\\" + name_and_extension[1] + "\\" + file)
            myOS.rename(origin_directory + "\\" + file, destination_directory + "\\" + name_and_extension[1] + "\\" + file)
            counter_moved_files = counter_moved_files + 1

sort_files_to_folders(unsorted_file_directory, sorted_directory)
print("Folders created: " + str(counter_folders_created))
print("Moved files: " + str(counter_moved_files))