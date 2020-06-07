#Object orientred programming
print("OOP")

class Dog():

    #Class object attribute - Same for any instance
    #Example all dogs are memmals

    #Fixed attribute
    species = "mammal"

    #Constructor
    def __init__(self,breed,name,spots):    #breed=parameter/argument
        self.breed = breed                  #self.breed is attribute
        self.name = name                    #By convention all shoud be same
        
        #Expect boolean
        self.spots = spots

    #Methods - Functions defined inside of the class
    def bark(self, number):
        for i in range(number):
            print(f"Vau-vau! Who is the good boy? {self.name}!")
        

my_dog = Dog(breed = "Gravhund", name = "Duplo", spots = False)
print(my_dog.breed)
my_dog.bark(2)

class Circle():
    
    #Class object attribute
    pi = 3.14       #Stndard use Circle.pi instead self.pi

    #Constructior - (With default value)
    def __init__(self, radius=1):
        self.radius = radius
        self.area = radius**2*Circle.pi

    #Method    
    def get_circumference(self):
        return self.radius * Circle.pi * 2

my_circle = Circle(3)

print(my_circle.radius)
print(my_circle.get_circumference())
print(my_circle.area)

#Inheritance (Naslijedjivanje)
print("Inheritance")
#Base class
class Animal():
    def __init__(self):
        print("Animal created")
    def who_am_i(self):
        print("I am an animal")
    def eat(self):
        print("I am eating")
    def speak(self):
        raise NotImplementedError("Subclass must be implemented")

#Derived class
class Cat(Animal):      #Inherit animal
    
    def __init__(self):
        Animal.__init__(self)
        print("Cat created")
    
    def who_am_i(self):     #Overwrite method from animal
        print("I am a cat")
    
    def miau(self):
        print("Miiiijaaaauuu")  #Extend

my_cat=Cat()
my_cat.eat()
my_cat.who_am_i()
my_cat.miau()

#Polimorphism
#Different object
print("Polimorphism")
class Cow():

    def __init__(self,name):
        self.name = name

    def speak(self):
        print(f"{self.name} says muuu")

class Chicken():
    def __init__(self,name):
        self.name = name
    def speak(self):
        print(f"{self.name} says kukuriku")

biserka = Cow("Biserka")
koka = Chicken("Koka")

biserka.speak()
koka.speak()

#Both classes can speak! for loop counts on that!
for pet_class in [biserka,koka]:
    print(type(pet_class))
    print(type(pet_class.speak))
    pet_class.speak()

#Example 2 -NOTE NOTE!!!  
def pet_speak(pet): #Doesn't know/care if pet is chicken or cow
    pet.speak()     #More common in Ploimorphisam, you would make function for something supported by base classe
                    #Then use it for derived classes

pet_speak(koka)


#Special methods
print("Special methods")
my_list = [1,2,3]
len(my_list)

#What if I want my class to be "covered" by len

class Book():

    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    def __str__(self):  #Dunder methods
        return f"{self.title} by {self.author}"
    def __len__(self):
        return self.pages
    def __del__(self):
        print("A book object has been deleted")

b = Book("Hlapic", "I.B.M.", 130)
print(b)    #If you ask for string of the object
print(len(b))     #If you ask for lenght of the object

del b #Delete variable - instance