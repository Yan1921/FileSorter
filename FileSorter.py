import os as myOS

#ToDo:
#Make file executable whereever is is stored (create all the folders necessary)

unsorted_file_directory = str(r"Testfolder")        	#Directory with stuff to be sorted
sorted_directory = str(r"Testfolder\sortedFolders")     #Path where sorted folders will go

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
        newfolder = str(f"{destination_directory}\{extension}")
        if not myOS.path.exists(newfolder):
            myOS.mkdir(newfolder)
            print(f"{extension} <-- Folder successfully created!")
            counter_folders_created = counter_folders_created + 1
        else:
            print(f"{extension} <-- Folder already exists!")

def sort_files_to_folders(origin_directory, destination_directory):
    global counter_moved_files
    create_folders_for_given_extensions(origin_directory, destination_directory)
    for file in myOS.listdir(origin_directory):
        name_and_extension = myOS.path.splitext(file)
        full_origin = str(f"{origin_directory}\{file}")
        full_destination = str(f"{destination_directory}\{name_and_extension[1]}\{file}")
        if name_and_extension[1] != "" and not myOS.path.exists(full_destination):
            myOS.rename(full_origin, full_destination)
            counter_moved_files = counter_moved_files + 1
        elif myOS.path.exists(full_destination):
            print(f"{file} <-- already exists at destination!")

sort_files_to_folders(unsorted_file_directory, sorted_directory)
print(f"Folders created: {str(counter_folders_created)}")
print(f"Moved files: {str(counter_moved_files)}")