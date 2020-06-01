# Comparator operators
import string


3 == 3
"hello" != "bye"
"2" != 2
"Hello" != "hello"
3 != 2
3 > 2
3 < 4
3 >= 2
3 <= 3

#Logical operators AND, OR, NOT. Comparators forst then logic
print((1 > 2) and (1==1))
print((1 > 2) or (1==1))
print(not(1 > 2) and (1==1))

#Statements
#IF
a = 2
if a == 0:
	print("if")
elif a == 1:
	print("elif")
else:
	print("else")
#For loops
#For everything iterable - list, string
iterable = ["one","two",3]
for item in iterable:
	print(item)

listoftuples = {(1,2),(3,4),(5,6),(7,8)} #list of tuples - Very often python structure 
len(listoftuples) #=4
for x in listoftuples:
	print(x)

for a,b in listoftuples: #"Tuple unpacking!" a nd b as two variables
	print(a)
	print(b)

#for loop dictionary
dictionary = {"k1":1,"k2":2,"k3":3}
for item in dictionary:	#iterates keys
	print(item)
for item in dictionary.items(): #iterates tuple pairs key + value (item=Key+Value(tuple))
	print(item)
for key,value in dictionary.items(): # iterates values
	print(value)

#While loops
print("While loop")
i=0
while i < 5 :
	print(i)
	i+=1
else:							#NOTE else for while!
	print("i is not below 5") 

#break = break closest enclosing loop
#continue = next iteration - Top of the closest enclosing loop.
#pass = nothing - Empty place holder after ":" there must be something

#Range(start,stop,step) - Generator (Function)
for num in range(10): 
	print(num)			#0,1,2,3,4,5,6,7,8,9
print("Next")
for num in range(5,10):
	print(num)			#5,6,7,8,9
print("Next")
for num in range(0,10,2):
	print(num)			#0,2,4,6,8
print("Next")

list(range(5,10))

#Enumerate - function - Makes list of items as touple items with item and index
#Takes any enumerable object
index_count = 0
word = "abcd"
for letter in word:
	print(f"At index {index_count} is letter {letter}")
	index_count += 1
print("Next")

#[a,b,c,d] becomes [(0,a),(1,b),(2,c),(3,d)]
for ind,letter in enumerate(word):
	print(f"At index {ind} is letter {letter}")

#Zip function - Oposite of Enumerate
#If list not same lenght, zips until shortest
list1 = [1,2,3]
list2 = ["a","b","c"]

for item in zip(list1,list2):
	print(item)

#In
print(1 in [1,2,3,4])
print("a" in "World")
print("k1" in dictionary.keys())
print(1 in dictionary.values())

#min max
print(min(list1))
print(max(list1))

#Random
from random import shuffle #include built in function from library
print(shuffle(list1)) #Return none "Null" actual change on the list, always different
print(list1) 

#Input
#result = input("Enter number here: ")  #Comes back as string!
#float(result) 			#Casting
#int(result)				#Casting
#print(type(result))		#It still string cast returns casted value as function result
#print(f"You entered {result}")

#List comprehensions - That's something
#For loop + .append()
string1 = "hello"

list3 = []
for letter in string1:
	list3.append(letter)
print(list3)

list4 = [letter for letter in string1]
print(list4)

list5 = [x**2 for x in range(0,11)] #appending all from for loop result
print(list5)

list6 = [x for x in range(0,11) if x%2==0]
print(list6)

celsius = [0,10,20,34.5]
fahrenheit = [(((9/5))*temp + 32) for temp in celsius]
print(fahrenheit)

#Nested loop
list7 = []
for x in [1,2,3]:
	for y in [10,20,30]:
		list7.append(x*y)

list8 = [x*y for x in [1,2,3] for y in [10,20,30]]
print(list7)
print(list8)


#TEST
st = 'Sam Print only the words that start with s in this sentence'
for word in st.split(" "):
    if word[0].lower() == "s":
        print(word)

for num in range(1,11):
    if num%2 == 0:
        print(num)
    
list(range(0,11,2))

st = 'Print every word in this sentence that has an even number of letters'
print([word for word in st.split() if len(word)%2 == 0])

for num in range(1,101):
    if (num%3 == 0) and (num%5 == 0):
        print("FizzBuzz")
    elif num%3 == 0:
        print("Fizz")
    elif num%5 == 0:
        print("Buzz")
    else:
        print(num)

st = 'Create a list of the first letters of every word in this string'
[word[0] for word in st.split()]