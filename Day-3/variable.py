#without variable
print("ec2_project_xyz")   #used for immediate output of any task .

#with variable
ec2_instance_name ="ec2_project_abc"  #for store values and reuse them later in your code.
print(ec2_instance_name)
print(ec2_instance_name)
print(ec2_instance_name)
print(ec2_instance_name)
print(ec2_instance_name)






# if you want to create a variable that is access inside maultiple varibale then make global scope variable
a=2   #global scope variable                                                     
b=2
def addition():
    print(a+b)

def substraction():
    print(a-b)

addition()
substraction()


#if you want to create a variable that is access only inside one funciton then create localscope  variable
a=2                                                  
b=2
def addition():
    c=10 #local scope variable
    print(a+b+c)

def substraction():
    print(a-b)

addition()
substraction()


    
