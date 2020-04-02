from staff import *
from food import *
from animal import *
from observation import *
from feeding import *
from terminaltables import AsciiTable
import datetime
import os

def addStaff(): pass

def printAnimals(): 
    data = [['Number', 'Gender', ]]
    for a in animalList: data.append([a.aNo, f.manufacturer])
    print(AsciiTable(data).table)
    selection = int(input("Press 1 to go back: "))
    if selection == 1: menu()
    else: 
        os.system('cls||clear')
        printStaff()

 
def printStaff():
    data = [['ID', 'Name', 'Surname', 'Office', 'Tel']]
    for s in staffList: data.append([s.id,s.fName,s.lName,s.office,s.tel])
    print(AsciiTable(data).table)
    selection = int(input("Press 1 to go back: "))
    if selection == 1: menu()
    else: 
        os.system('cls||clear')
        printStaff()
    

def printFood():
    data = [['Food Name', 'Manufacturer']]
    for f in foodList: data.append([f.foodName, f.manufacturer])
    print(AsciiTable(data).table)
    selection = int(input("Press 1 to go back: "))
    if selection == 1: menu()
    else: 
        os.system('cls||clear')
        printStaff()

def menu():
    print("Welcome to the Institute Tracking Application!")
    print("---MENU---")
    selection = 1 #need to initialize to make system(clear) work
    print(AsciiTable([['Select', 'Action'],
            ['1', 'Existing Staff Details'],
            ['2', 'Existing Animal Details'],
            ['3', 'Existing Food Details'],
            ['4', 'Create Animal Feeding Report'],
            ['5', 'Create Animal Observation Report'],
            ['6', 'Add a new staff'],
            ['7', 'Add a new animal'],
            ['8', 'Add a new food item']]).table)
    selection = int(input("Selection: "))
    if selection not in range(1,9):
        os.system('cls||clear')
        print('Invalid selection!')
        menu()
    elif selection == 1: printStaff()
    elif selection == 2: printAnimals()
    elif selection == 3: printFood()
    elif selection == 6: addStaff()
    

if __name__ == '__main__':

    staffList = []
    foodList = [] 
    animalList = []
    #foodList.append(Food("Gofret", "Eti"))
    staffList.append(Staff("0", "Kerem", "Cömert", "A-123", "1234"))
    staffList.append(Staff("1", "Yiğit", "Aslı", "A-124", "1325"))
    menu()
    
    #printStaff()
    #printFood()