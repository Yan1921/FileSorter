import os as myOS

unsorted_file_directory = str(myOS.getcwd())        	     #Directory with stuff to be sorted
sorted_directory = str(f"{myOS.getcwd()}\sortedFiles")     #Path where sorted folders will go

counter_folders_created = 0
counter_folders_not_created = 0
counter_moved_files = 0
counter_not_moved_files = 0
ignored_extensions = [".py", ".txt", "", ".md"]

def getextensions(directory):
     extensions = []
     for file in myOS.listdir(directory):
        name_and_extension = myOS.path.splitext(file)
        if name_and_extension[1] != "":
            extensions.append(name_and_extension[1])
     return(extensions)

def create_folders_for_given_extensions(origin_directory, destination_directory):
    global counter_folders_created
    global counter_folders_not_created
    extensions = set(getextensions(origin_directory))
    if not myOS.path.exists(destination_directory):
        myOS.mkdir(destination_directory)
        counter_folders_created = counter_folders_created + 1
        print("sortedFiles folder created!")
    else:
        counter_folders_not_created = counter_folders_not_created + 1
    for extension in extensions:
        newfolder = str(f"{destination_directory}\{extension}")
        if not myOS.path.exists(newfolder) and extension not in ignored_extensions:
            myOS.mkdir(newfolder)
            print(f"{extension} <-- Folder successfully created!")
            counter_folders_created = counter_folders_created + 1
        else:
            print(f"{extension} <-- Folder already exists!")
            counter_folders_not_created = counter_folders_not_created + 1

def sort_files_to_folders(origin_directory, destination_directory):
    global counter_moved_files
    global counter_not_moved_files
    create_folders_for_given_extensions(origin_directory, destination_directory)
    for file in myOS.listdir(origin_directory):
        name_and_extension = myOS.path.splitext(file)
        full_origin = str(f"{origin_directory}\{file}")
        full_destination = str(f"{destination_directory}\{name_and_extension[1]}\{file}")
        if name_and_extension[1] != "" and not myOS.path.exists(full_destination) and name_and_extension[1] not in ignored_extensions:
            myOS.rename(full_origin, full_destination)
            counter_moved_files = counter_moved_files + 1
        elif myOS.path.exists(full_destination):
            print(f"{file} <-- already exists at destination!")
            counter_not_moved_files = counter_not_moved_files +  1

sort_files_to_folders(unsorted_file_directory, sorted_directory)
print(f"Folders created: {str(counter_folders_created)}")
print(f"Moved files: {str(counter_moved_files)}")
print(f"Folders not created: {str(counter_folders_not_created)}")
print(f"Not moved files: {str(counter_not_moved_files)}")