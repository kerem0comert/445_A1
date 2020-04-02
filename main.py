from staff import *
from food import *
from animal import *
from observation import *
from feeding import *
from terminaltables import AsciiTable
import datetime
import os
import sys
sourcefile = "place_holder"  #Global variable-source txt file's name
def loadfile():
    global sourcefile
    if sys.argv[1:]==[]:       #if there is no argument entered in terminal
        sourcefile=input("There is no argument!\nEnter a name for txt file to be created:")
    else:                     #if there is an extra argument in terminal
        print(f"The source txt file name is {sys.argv[1]}\n")
        sourcefile=sys.argv[1]      #no error checks - sourcefileNotFound, TooManyArguments SHALL BE ADDED

def readTxtFile():            #staff read is done, waiting for animal and food add functions to be added to implement them
    fo= open(sourcefile,"r+")
    fl=fo.readlines()
    for ln in fl:
        if ln.startswith("S:"):
            step_0=ln.split(":")
            step_1=step_0[1]
            step_2=step_1.split(",")
            staffList.append(Staff(step_2[0],step_2[1],step_2[2],step_2[3],step_2[4]))       
        #if ln.startswith("A:"):
            #step_0=ln.split(":")
            #step_1=step_0[1]
            #step_2=step_1.split(",")
            #animalList.append(Animal(step_2[0],step_2[1],step_2[2],step_2[3],step_2[4])) 
    fo.close()      

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
    loadfile()     #Finds or creates source txt file
    readTxtFile()  #Reads from source file to according staff,animal or food lists
    menu()
    
 