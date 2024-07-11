#mutable --it mean it can be changeble

#for printing a list this take a lot of time
student1 ="payal"
student2 ="ram"
student3 ="sonu"
student4 ="dev"
student5 ="anshal"

print(student1)
print(student2)
print(student3)
print(student4)
print(student5)


#with using list
students_names = ["payal","ram","sonu","dev","anshal"]
print(students_names)



#list s3 bucket
s3_bucket_list = ["payal_demo_bucket","anshal_demo_bucket"]
print(type(s3_bucket_list))



#append -add new item 
s_names = ["payal","ram","sonu","dev","anshal"]
s_names.append("hit")
print(s_names)



#remove -remove item from the list
s_names = ["payal","ram","sonu","dev","anshal"]
s_names.remove("sonu")
print(s_names)



#to print prticular item name 
s3_bucket_list = ["payal_demo_bucket","sonu_demo_bucket","anshal_demo_bucket","dev_demo_bucket"]
print(s3_bucket_list[0])
print(s3_bucket_list[-1])

#print length of list  and then append one more item and see result then remove one item and see result
s3_bucket_list = ["payal_demo_bucket","sonu_demo_bucket","anshal_demo_bucket","dev_demo_bucket"]
print(len(s3_bucket_list))

s3_bucket_list.append("hit_demo_bucket")
print(len(s3_bucket_list))

s3_bucket_list.remove("payal_demo_bucket")
print(len(s3_bucket_list))


#slicing of list

s3_bucket_list = ("payal_demo_bucket","sonu_demo_bucket","anshal_demo_bucket","dev_demo_bucket")
print(s3_bucket_list[1:-1])

#sorting in list
num=[10,55,9]
num.sort()
print(num)

#concatination in list
s3_bucket_list = ("payal_demo_bucket","sonu_demo_bucket","anshal_demo_bucket","dev_demo_bucket")
print(s3_bucket_list[0]+ "--" +s3_bucket_list[1])












