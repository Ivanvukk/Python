a = 3								#Integer
b = 2.3 							#Float
c = "hello"							#String can be also 'hello', ordered sequenc eof characters
d = [10,"hello",200.3] 				#List - Ordered sequence of objects
e = {"key":"value","name":"Andy"}	#Dictionary - Value pairs
f = (10,"hello", 200.3) 			#Tuples - Ordered imutable sequence
g = {"a","b"}						#Sets - Unordered collection of unique objects
h = True							#Boolean

#Accessing
print(a)
print(b)
print(c)
print(d[0],d[1],d[2], d[-1])
print(1/2)

#Maths 1/2=0.5!

#Variables
#Can't start with number, no spaces, lowercase, no special characters
#Dynamic typing - Same variable changes datatype. Use type()
type(a)

#String - you can access characters by indexing (from zero) c[-1]= last character
test_str = "abcdefghijklmn" #uses double since single is in string
print("hello \n world")
print(len("test_str"))
print(test_str[4:]) #From index (including!) for until the end -> efgh...
print(test_str[:4])	#Until the index (excluding!)->abcd (indexes 0,1,2,3)
print(test_str[2:4]) 	#=cd
print(test_str[3:6])	#=def 
print(test_str[::2])	#take every other =ace...
print(test_str[::-1])	#reverse string ;)
print("Hello" + ' ' + "World") #String concatination
#Strings are immutable, can't change it -> make new one.
print("Hello world,"*3) #Multiplication work as well
#String methods and properties
x = "Hello World"
print(x.upper())
print(x.lower())
x.split() #split on white space, can split on any character, put them in a list
#Print tricks
print("Hi {}! {}".format('Ivan', "How are you?"))
print("Hi, {1} {0}?".format('Ivan', 'How are you'))
print("Hi, {i} {h}?".format(i='Ivan', h='How are you')) # can repeat same

result=100/3
print("the result is {r:2.2f}".format(r=result))

#f-strings - Write varible directly in string like in C# @""
print(f"The reuslt is {result:2.2f}")

#Lists
my_list = [1,2,3]
my_list = ["string",100,23.5] #You can mix up everything - List of objects
my_list = ["one","two","three","four"]

print(my_list[2:])

my_list[0] = "ONE" #Objects can be chenged compared to strings
print(my_list)
my_list.append("five")
print(my_list)
popped_item = my_list.pop() #Took last one - Result is the object which is removed
print(my_list)
my_list.pop(0)	#Remove at index
print(my_list) #NOTE list changed!
new_list = [4,6,1,4,0,2]
new_list.reverse() #Note reverse sort, just reverse
print(new_list)
new_list.sort() #Returns "None" value, comes back from function "void", no result 
print(new_list)
new_list.reverse()
print(new_list)

#Dictionries - Address objects by key instead index, don't care hwre it is
#No sorting, but easy access

my_dict = {"apple":2.66, "orange":8.12}

print(my_dict["apple"])

#Flexible in datatypes - can hold lists, other dictionries
my_dict = {"k1":[1,2,3], "k2":{"k2.1":"a","k2.2":"b"}}
print(my_dict["k2"]["k2.2"].upper())	#Not actually changed in dict- just result
print(my_dict["k2"]["k2.2"])			#Addressing dict inside dict
my_dict.keys()
print(my_dict.values())
my_dict.items()				#comes in tuples

my_dict["k3"] = 500			#add new item
print(my_dict)

#Tuples - Tupls-Tapls like lists, just () istead []
#They cannot be changed! Immutable, othervise similar to lists

t = (1,2,3)
l = [1,2,3]
print(type(t))
print(type(l))
len(t)

#Slicing, indexing, like lists
print(t.count(2))	#How many times "2" is in tuple
print(t.index(2))	#find index of 2
#Why use them at all? Data ntegrity, make sure function doesn't change your sequence

#Sets - sequence of UNIQUE elements
print("sets")
s = set()
s.add(1)
print(s)
s.add(2)
print(s)
s.add(2) 		#NOthing happens
#cast list to set to get only unique elements of list :)
set("Mississippi") 		#Filters duplicates

#Booleans
#Make sure they are capitalised "True" & "False"
print("Booleans") 	#bool
print(1 > 2) 		#returns False
b = None 			#Like Null
b = 1 > 2
print(f"{type(b)} & value: {b}")


#Files
print("I/O Files")
my_file = open("testFile.txt")
print(my_file.read())
my_file.seek(0)			#If you need to reed again, you need to reset cursor!!!
print(my_file.readlines())	#List of lines - \n is still there!

#Openning file which is not in same location as python. Double \\ like C
my_file = open("C:\\Users\\Marina\\Desktop\\Python\\testFile.txt")
my_file.close()	#You have to close it

#Best practce - Similar to C# when using database
with open("testFile.txt") as my_new_file:
	contents = my_new_file.read()

my_file = open("testFile.txt", mode="r")	#Read - Default
my_file.close()
#r, w (write, or new if not there), a (append) 
with open("testFile.txt", mode='a') as my_new_file:
	my_new_file.write("four on fourth\n")







