import os
# folders sys.argv[1]  - read input through command line

#read input from the user -at runtime
folders = input("please provide a list of folder names with spaces in between:").split()
print(folders)

#list file in folder
for folder in folders:
    try:
        files = os.listdir(folder)   #os is identity module
    except FileNotFoundError:         #exception handling
     print("provide a valid folder name  look like folder is not exist:" +folder)
     break
    except PermissionError:
     print("no access to  this folder:" +folder)


     print(" ===listing file for folder - "+ folder)
     
     for file in files:
          print(file)  #print file




#using function
import os

def list_files_in_folder(folder_path):
    try:
        files = os.listdir(folder_path)
        return files, None
    except FileNotFoundError:
        return None, "Folder not found"
    except PermissionError:
        return None, "Permission denied"

def main():
    folder_paths = input("Enter a list of folder paths separated by spaces: ").split()
    
    for folder_path in folder_paths:
        files, error_message = list_files_in_folder(folder_path)
        if files:
            print(f"Files in {folder_path}:")
            for file in files:
                print(file)
        else:
            print(f"Error in {folder_path}: {error_message}")

if __name__ == "__main__":
    main()



