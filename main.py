from staff import *
from food import *
from terminaltables import AsciiTable
import datetime

def printStaff(sList):
    data = [['ID', 'Name', 'Surname', 'Office', 'Tel']]
    for s in sList: data.append([s.id,s.fName,s.lName,s.office,s.tel])
    print(AsciiTable(data).table)

def printFood(fList):
    data = [['Food Name', 'Manufacturer']]
    for f in fList: data.append([f.foodName, f.manufacturer])
    print(AsciiTable(data).table)

if __name__ == '__main__':
    staffList = []
    foodList = []
    foodList.append(Food("Gofret", "Eti"))
    staffList.append(Staff("0", "Kerem", "Cömert", "A-123", "1234"))
    staffList.append(Staff("1", "Yiğit", "Aslı", "A-124", "1325"))
    printStaff(staffList)
    printFood(foodList)