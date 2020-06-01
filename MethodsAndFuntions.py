#Functions

def next():
    '''
    DOCSTRING: Prints "Next"
    INPUT: none
    OUTPUT: none
    '''
    print("Next")

list1 = [1,2,3]
print(list1)
next()

def add_fnc(a,b):
    '''
    DOCSTRING: Prints "Next"
    INPUT: a,b
    OUTPUT: a+b
    '''
    return a + b

print(add_fnc(1,4))

def say_hello(name="name"): # Default accours if you don't provide input
    '''
    No description
    '''
    print("Hello " + name)

say_hello("Ivan")

print(add_fnc("a","b"))

print("dog" in "My Dog's name is Charlie".lower()) #Using in

#Pig latin translator
def pig_latin(word):
    '''
    Translates to pig latin
    '''
    if word[0] in 'aeiou':
        return  word + "ay"
    else:
        return word[1:] + word[0] + "ay"

print(pig_latin("apple"))
print(pig_latin("word"))

#*args and **kwargs arguments and keywordarguments
#Arbitrary arguments
def myfunc(a,b):
    #Returns 5% of sum a b
    return sum((a,b))*0.05

print(myfunc(40,60))

def myargs(*args):  #Takes arguments as TUPLES
    return sum(args) * 0.05

def mykwargs(**kwargs):  #Takes arguments as DICTIONARY
    if "fruit" in kwargs:
        print("My fruit of choice is {}".format(kwargs["fruit"]))
    else:
        print("No fruits here")

mykwargs(fruit="apple", veggie="lettuce")

def combo(*args,**kwargs):
    print(args)
    print(kwargs)

combo(10,20,30, fruit="apple", animal="dog")

def myfunc5(input_string):
    mystring = ""
    for ind,letter in enumerate(input_string.lower()):
        if (ind + 1)%2 == 0:
            mystring += letter.lower()
        else:
            mystring += letter.upper()
            
    return mystring

print(myfunc5("AnacOndA"))

for i in range(2,3):
    print(i)

#Maps - Apply function on each element of inerable
print("Maps")
def square(num):
    return num**2

my_nums = [1,2,3,4,5,6]

for item in map(square,my_nums):
    print(item)

print(list(map(square,my_nums))) #Makes list of it
print([x**2 for x in my_nums]) #Does the same

#Filter function - Filter iterable based on function
print("Filters")
def check_even(num):
    return num%2 == 0

print(list(filter(check_even,my_nums)))

#Lambda exressions - Annonimus function
print("Lambda")

print(list(map(lambda num: num ** 2, my_nums)))
print(list(filter(lambda num: num%2 == 0, my_nums)))

names = ["Marina", "Ivan", "Teja"]
print(list(map(lambda x:x[::-1],names)))

#Nested statemens and scope
print("Scope")
x = 50
def printx(x):
    print(f"X is {x}")
    #Local reasigment
    x=300
    print(f"After local reasigment X is {x}")

printx(x)
print(f"Reasigment didn't happen for X outside of function X is {x}")

                    #Fourts it looks for built-in (B)
y = 10              #Third it looks for global (G)
def printy():
    y = 20          #Second it looks for enclosure (E)
    def printy2():
        y = 30      #First it looks for local (L)
        print(y)
    printy2()

printy()

#Above is aways call by value
#Call by reference example

z=5
def changeZ():
    global z        #Generally avoid this
    z=10
changeZ()
print(z)

#Correct would be
u=100
def changeU(u):
    u = 200
    return u
u = changeU(u)
print(u)

s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
def countUL(s):
    d={"upper":0, "lower":0}

    for c in s:
        if c.isupper():
            d["upper"] += 1
        elif c.islower():
            d["lower"] += 1
        else:
            pass
    
    print(f'Number of lower case characters {d["lower"]}')
    print(f'Number of upper case characters {d["upper"]}')

countUL(s)

#Pangram check
import string
lst_of_lowercase = list(string.ascii_lowercase)
print(lst_of_lowercase)
check_pangram = "The quick brown fox jumps over the lazy dog"

for c in check_pangram:
    if c in lst_of_lowercase:
        lst_of_lowercase.remove(c)
if len(lst_of_lowercase) == 0:
    print("Sentence is pangram")

