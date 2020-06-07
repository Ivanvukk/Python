def my_func():
    print("Hey I am in MyModule.py")

    if __name__ == "__main__":
        print("This script is run as main.\nIt's the one called from cmd")
    else:
        print("This is called as module (Imported). Not directly from the cmd")