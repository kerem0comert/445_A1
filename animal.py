from terminaltables import AsciiTable
from environment import *

class Animal:
    observationRecord = []
    feedingRecord = []
    def __init__(self, no, gender, doB, color, environment):
        self.no = no
        self.gender = gender
        self.doB = doB
        self.color = color
        self.environment = environment

    def printDetails(self):
        print("\n========OBSERVATION RECORDS=========")
        data = [['Date', 'Time', 'Weight', 'Temperature', 'Note', 'Staff']]
        for record in self.observationRecord: data.append([record.date, record.time, record.aWeight, record.temperature, record.note, record.staff])
        print(AsciiTable(data).table)
        print("\n==========FEEDING RECORDS===========")
        data = [['Date', 'Time', 'Food', 'Staff']]
        for record in self.feedingRecord: data.append([record.date, record.time, record.food, record.staff])
        print(AsciiTable(data).table)
        print("\n============ENVIRONMENT=============")
        data = [['Humidity', 'Size', 'Temperature', 'Hours of light']]
        data.append([self.environment.humidity, self.environment.size, self.environment.temperature, self.environment.h_of_light])
        print(AsciiTable(data).table)
        input("Press Enter to continue...")

    
    @staticmethod
    def chooseEnvironment(environmentList,sourcefile):
        No = 1
        data = [['No', 'Humidity', 'Size', 'Temperature', 'Hours of light']]
        for a in environmentList:
            data.append([No, a.humidity, a.size, a.temperature, a.h_of_light])
            No += 1
        print(AsciiTable(data).table)
        selection = int(input("Select the number of environment you want to add (type 0 to add new one): "))
        if (selection == 0):
            theNewEnvironmet = Environment.create(sourcefile,environmentList)
            environmentList.append(theNewEnvironmet)
            return theNewEnvironmet
        else:
            return environmentList[selection - 1]

    @staticmethod
    def create(environmentList,sourcefile):
        no = input("Enter No: ")
        gender = input("Enter Gender: ")
        doB = input("Enter Date of Birth: ")
        color = input("Enter Color: ")
        Environment_animal=Animal.chooseEnvironment(environmentList,sourcefile)
        fo=open(sourcefile,"a+")
        fo.write("\nA:%s,%s,%s,%s,%s" % (no,gender,doB,color,Environment_animal.environmentID))
        fo.close()
        return Animal(no, gender, doB, color, Environment_animal)