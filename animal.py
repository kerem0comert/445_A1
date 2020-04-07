from terminaltables import AsciiTable
from environment import *
from observation import *
import time

DAY = 24*60*60

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
        
        print("\n========ANIMAL=========")
        data = [['no', 'gender', 'doB', 'color'],[self.no, self.gender, self.doB, self.color]]
        print(AsciiTable(data).table)
        print("\n========OBSERVATION RECORDS=========")
        data = [['Date', 'Time', 'Weight', 'Temperature', 'Note', 'Staff']]
        for record in self.observationRecord: data.append([record.observationDate, record.observationTime, record.aWeight, record.temperature, record.note, record.staff.fName + " " + record.staff.lName])
        print(AsciiTable(data).table)
        print("\n==========FEEDING RECORDS===========")
        data = [['Date', 'Time', 'Food Name', 'Manufacturer', 'Weight', 'Staff']]
        for record in self.feedingRecord: data.append([record.date, record.time, record.food.foodName, record.food.manufacturer, record.weight, record.staff.fName + " " + record.staff.lName])
        print(AsciiTable(data).table)
        print("\n============ENVIRONMENT=============")
        data = [['Humidity', 'Size', 'Temperature', 'Hours of light']]
        data.append([self.environment.humidity, self.environment.size, self.environment.temperature, self.environment.h_of_light])
        print(AsciiTable(data).table)

        currentTimeStamp = int(time.time()) 
        
        observationCount = sum(currentTimeStamp - int(o.unixTimeStamp) < DAY for o in self.observationRecord)
        if observationCount < 3:
            print("Today, this animal has been observed {} times. "
                  "Please make sure to observe it 3 times before today ends.".format(observationCount))
       
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


    def addObservation(self, sourcefile, staffList): 
        self.observationRecord.append(Observation.create(self.no,sourcefile,staffList))

    def addFeeding(self, sourcefile, staffList, foodList): 
        
        #for this to work properly, all the different machines that are running this code
        #must have synchronized date and times locally. By assumption, this is UTC
        currentTimeStamp = int(time.time()) 
        counter = sum(currentTimeStamp - int(f.unixTimeStamp) < DAY for f in self.feedingRecord)
        if counter > 2: 
            print("You already fed this animal {} times today!".format(counter))
            return

        feedingDate = datetime.datetime.today().strftime("%d/%m/%Y")
        feedingTime = datetime.datetime.now().strftime("%H:%M")

        self.feedingRecord.append(Feeding.create
                                  (self.no,sourcefile,staffList, foodList, feedingDate, feedingTime, currentTimeStamp))
