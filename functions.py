from math import sqrt


def my_fun():
    #pass #this does nothing, but all functions need something inside
    print("Hello World")
my_fun()

a = my_fun
a()

#Feb 10
def my_fun(to_print):
    print(to_print)
a = my_fun
a("hello world")
c = 3+7.4838293
print(c)
to_print = f"{c:.2f}"
a("hello world")
print(to_print)

def pyth(a,b):
    c2 = a**2+b**2
    return sqrt(c2)

def pyth2(a,b=None): #can provide default values
    if b == None:
        b = a
    c2 = a**2+b**2
    return sqrt(c2)

print(pyth(3,4))
print(pyth2(3))

def find(a_list,value):
    for i in range(0,len(a_list)):
        if a_list[i] == value:
            return (True,i) #tuple #return ends the loop immediately
    return (False,None)

a_list = [3,6,2]
print(find(a_list,6))
found,index = find(a_list,6) #prints if it found it and the location
print(found,index)



