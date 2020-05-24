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

listoftuples = {(1,2), (3,4),(5,6),(7,8)} #list of tuples - Very often python structure 
len(listoftuples) #=4
for x in listoftuples:
	print(x)

for a,b in listoftuples: #"Tuple unpacking!" a nd b as two variables
	print(a)
	print(b)

dictionary = {"k1":1,"k2":2,"k3":3}

for item in dictionary:	#iterates keys
	print(item)
for item in dictionary.items(): #iterates tuple pairs key + value (item=Key+Value(tuple))
	print(item)
for key,value in dictionary.items(): # iterates values
	print(value)

