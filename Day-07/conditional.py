import sys

type = sys.argv[1]
if type == "t2.micro":
    print("ok,we will charge you 2 dollers")
elif type == "t2.meadium":
     print("ok,we will charge you 4 dollers")
elif type == "t2.xlarge":
    print("ok,we will charge you 6 dollers")
else:
    print("provide valid instance name")


    
