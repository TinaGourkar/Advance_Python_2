# This is Python script i.e a .py file
print("Welcome!!")

for i in range(1,25):
    print(f"This is {i}")

def add(x,y):    
    ''' 
    Input : two input will be given in the fuction add()
    Output : The addition of two numbers will be given  
    '''
    a = x + y
    print(f"The Addition of two number is {a}")

add(21,12)

def simple_intrest(p,n,r):  
    '''
    Input : Principle, Number of years and rate of intrest will be given as input in a function
    Output : By applying simple intrest formula we will get an output
    '''  
    si = (p*n*r)/100
    print(si)

simple_intrest(52000,3,4.9)
simple_intrest(2000,3,4.9)


# self example for no reason
def self(m):
    for i in range(1,m):
        print(f"Hey, i am repeating m times i.e i am {i}")

self(5)
self(100)

# this is addition by return method
def add(x,y):    
    ''' 
    Input : two input will be given in the fuction add()
    Output : The addition of two numbers will be given  
    '''
    add = x + y    # idk but giving same name as function name is working???
    return add

addition = add(21,20)
print(addition)