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



