from terminaltables import AsciiTable
from environment import *
from observation import *
import time
import os
import re

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
            print("\nToday, this animal has been observed {} times. "
                  "Please make sure to observe it 3 times before today ends.".format(observationCount))
       
        data = [['Selection', 'Action'],
                ['1', 'Feeding details between specified dates'],
                ['2', 'Observation details between specified dates'],
                ['3', 'All staff that observed this animal'],
                ['4', 'All food that were given to this animal'],
                ['5', 'Continue']]
        print(AsciiTable(data).table)
        selection = 0
        selection = int(input("Selection: "))
        if selection == 1:   self.specifiedFeeding()
        elif selection == 2: self.specifiedObservation()
        elif selection == 3: self.uniqueStaff()
        elif selection == 4: self.uniqueFood()
        elif selection == 5: return
        else: 
            print("Invalid selection.")
            self.printDetails()
    
 
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

    
    def specifiedFeeding(self):
        startDate, endDate = self.dateSelector()
        print("\n==========FEEDING RECORDS ({} and {})===========".format(startDate, endDate))
        data = [['Date', 'Time', 'Food Name', 'Manufacturer', 'Weight', 'Staff']]
        for record in self.feedingRecord: 
            if startDate.timestamp() <= float(record.unixTimeStamp) <= endDate.timestamp():
                data.append([record.date, record.time, record.food.foodName, record.food.manufacturer, 
                            record.weight, record.staff.fName + " " + record.staff.lName])
        if len(data) == 1: print("No record found in the specified period.")
        else: print(AsciiTable(data).table)
        selection = input("Press 'E' to export details.\nPress Enter to continue...")
        if selection == 'e' or selection == 'E':
            with open("feed_a{}.txt".format(self.no), "w") as feedDetails:
                feedDetails.write(AsciiTable(data).table)
                print("Export successful.")

    def specifiedObservation(self):
        startDate, endDate = self.dateSelector()
        print("\n==========OBSERVATION RECORDS ({} and {})===========".format(startDate, endDate))
        data = [['Date', 'Time', 'Weight', 'Temperature', 'Note', 'Staff']]
      
        for record in self.observationRecord: 
            if startDate.timestamp() <= float(record.unixTimeStamp) <= endDate.timestamp():
                 data.append([record.observationDate, record.observationTime, record.aWeight, 
                             record.temperature, record.note, record.staff.fName + " " + record.staff.lName])
        if len(data) == 1: print("No record found in the specified period.")
        else: print(AsciiTable(data).table)
        selection = input("Press 'E' to export details.\nPress Enter to continue...")
        if selection == 'e' or selection == 'E':
            with open("obsv_a{}.txt".format(self.no), "w") as obsvDetails:
                obsvDetails.write(AsciiTable(data).table)
                print("Export successful.")
    

    def dateSelector(self):
        start = input("Select start date (dd/mm/yy): ")
        try: 
            startDate = datetime.datetime.strptime(start,"%d/%m/%y")
        except  ValueError as err:
            print(err)
            self.dateSelector()
        end = input("Select end date (dd/mm/yy): ")
        try: 
            endDate = datetime.datetime.strptime(end,"%d/%m/%y")
        except  ValueError as err:
            print(err)
            self.dateSelector()
        #cast date objects into unixTimeStamps and return.
        return startDate, endDate
    
    def uniqueStaff(self):
        print("\n========STAFF THAT OBSERVED THIS ANIMAL=========")
        data = [['ID', 'Name', 'Surname', 'Office', 'Tel']]
        uniqueStaffList = []
        for o in self.observationRecord: 
            if o.staff not in uniqueStaffList:
                data.append([o.staff.id,o.staff.fName,o.staff.lName,o.staff.office,o.staff.tel])
                uniqueStaffList.append(o.staff)
        print(AsciiTable(data).table)
        selection = input("Press 'E' to export details.\nPress Enter to continue...")
        if selection == 'e' or selection == 'E':
            with open("staff_a{}.txt".format(self.no), "w") as uniqueStaffDetails:
                uniqueStaffDetails.write(AsciiTable(data).table)
                print("Export successful.")

    def uniqueFood(self):
        print("\n========FOOD THAT WERE GIVEN TO THIS ANIMAL=========")
        data = [['ID', 'Name', 'Manufacturer']]
        uniqueFoodList = []
        for feeding in self.feedingRecord: 
            if feeding.food.foodID not in uniqueFoodList:
                data.append([feeding.food.foodID,feeding.food.foodName,feeding.food.manufacturer])
                uniqueFoodList.append(feeding.food.foodID)
        print(AsciiTable(data).table)
        selection = input("Press 'E' to export details.\nPress Enter to continue...")
        if selection == 'e' or selection == 'E':
            with open("feed_a{}.txt".format(self.no), "w") as uniqueFoodList:
                uniqueFoodList.write(AsciiTable(data).table)
                print("Export successful.")
