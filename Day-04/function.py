#without function use

num1 = 5
num2 = 5

addition = num1 + num2
print("value of addition- " + str(addition))

sub = num1 - num2
print("value of sub - " + str(sub))

mul = num1 * num2
print("value of mul - " + str(mul))

#with function use
num1 = 10
num2 = 5

def addition():
    add = num1 + num2
    print(add)


def sub():
    sub = num1 - num2
    print(sub)

def mul():
    mul = num1 * num2
    print(mul)


addition()
sub()
mul()


#take input,perform required logic and return the output

def addition(num1, num2):
    add = num1 + num2
    return add

def sub(num1, num2):
    sub = num1 - num2
    return sub


def mul(num1, num2):
    mul = num1 * num2
    return mul

print(addition(5,10))
print(sub(10,5))
print(mul(10,5))



