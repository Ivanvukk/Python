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

