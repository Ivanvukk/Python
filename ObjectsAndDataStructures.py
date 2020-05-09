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





