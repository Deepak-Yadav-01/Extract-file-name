import os

def get_file_names(folder_path):
    file_names = []
    for file in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, file)):
            file_names.append(file)
    return file_names

# Provide the folder path where the files are located
folder_path = "C:\Materials"

# Call the function to retrieve the file names
file_names = get_file_names(folder_path)

# Print the file names
for name in file_names:
    print(name)
