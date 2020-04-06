import datetime
from main import *

class Observation:
    def __init__(self,observationDate,observationTime,aWeight,temperature,note,staff):
        self.observationDate = observationDate
        self.observationTime = observationTime
        self.aWeight = aWeight
        self.temperature = temperature
        self.note = note
        self.staff = staff

    @staticmethod
    def create(observationRecord, sourcefile, staffList):
      observationDate = datetime.datetime.today().strftime("%d/%m/%Y")
      observationTime = datetime.datetime.now().strftime("%H:%M")
      aWeight = input("Enter animal weight: ")
      temperature = input("Enter temperature: ")
      note = input("Enter a note (not necessary): ")
      data = [['ID', 'Name', 'Surname', 'Office', 'Tel']]
      for s in staffList: data.append([s.id,s.fName,s.lName,s.office,s.tel])
      print(AsciiTable(data).table)
      selection = input("Select a staff by its ID: ")
      found = None

      while found is None:
        for staff in staffList:
            if selection == staff.id: found = staff
        if found is None:
            print("This staff doesn't exist in the database.")
            selection = input("Select a staff by its ID: ")

      return Observation(observationDate, observationTime, aWeight, temperature, note, staff)
