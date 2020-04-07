import datetime
from main import *
import time

class Observation:
    def __init__(self,observationDate,observationTime,aWeight,temperature,note,staff, unixTimeStamp):
        self.observationDate = observationDate
        self.observationTime = observationTime
        self.aWeight = aWeight
        self.temperature = temperature
        self.note = note
        self.staff = staff
        self.unixTimeStamp = unixTimeStamp

    @staticmethod
    def create(animalID,sourcefile, staffList):
      unixTimeStamp = int(time.time())
      observationDate = datetime.datetime.today().strftime("%d/%m/%Y")
      observationTime = datetime.datetime.now().strftime("%H:%M")
      aWeight = input("Enter animal weight: ")
      temperature = input("Enter temperature: ")
      note = input("Enter a note (not necessary): ")
      data = [['ID', 'Name', 'Surname', 'Office', 'Tel']]
      for s in staffList: data.append([s.id,s.fName,s.lName,s.office,s.tel])
      print(AsciiTable(data).table)
      selection = input("Select a staff by its ID: ")
      theStaff = None

      while theStaff is None:
        for staff in staffList:
            if selection == staff.id: theStaff = staff
        if theStaff is None:
            print("This staff doesn't exist in the database.")
            selection = input("Select a staff by its ID: ")
    
      fo=open(sourcefile,"a+")
      fo.write("\nO:%s,%s,%s,%s,%s,%s,%s,%d" % (observationDate,observationTime,
                                                aWeight,temperature,note,theStaff.id,animalID, unixTimeStamp))
      fo.close()
      return Observation(observationDate, observationTime, aWeight, temperature, note, theStaff, unixTimeStamp)
