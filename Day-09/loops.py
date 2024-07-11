#it's ok to print 1 or 3 line what when we want to print 10000 line it very time consuming also this is not right way
print("payal")
print("payal")
print("payal")


#using for loop
for i in range(10):
    print("payal daki")

#
for i in range(10):
    print(i)
    print("-payal")

#print list of item  using for loop
color = ["pink","blue","black"]
numbers= [1, 2, 3, 4, 5, 6, 7, 8, 9]
for x in color:
    print(x)

#
fruits = ["apple", "banana", "cherry"]
for f in fruits:
    print(f)


#for loop to find error in log file
log_file = [
   "INFO: Operation successful",
   "ERROR: File not found",
   "DEBUG: Connection established",
   "ERROR: Database connection failed",
]

for line in log_file:
   if "ERROR" in line:
       print(line)


#while loop
count = 0
while count < 5:
    print(count)
    count += 1





    
    
