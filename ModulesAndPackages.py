#Module = External .py script used in your script
#Package = Collection of modules

#Install external package from pipy-Official open source
#pip install X      e.g.X=requests - Used fo5 WEB API

#Make your own module!
#Include function from anouther script (Module)
from MyModule import my_func

#Call function from another script (Module)
my_func()

#Import from package
from MyMainPackage import  MyMainModule as main
from MyMainPackage.MySubPackage import MySubModule as sub

main.my_main_func()
sub.my_sub_func()

if __name__ == "__main__":
    print("This script is run as main.\nIt's the one called from cmd")
    