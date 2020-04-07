import datetime
from terminaltables import AsciiTable

class Feeding:
    def __init__(self, date, time, food, weight, staff, unixTimeStamp):
        self.date = date
        self.time = time
        self.food = food
        self.weight = weight
        self.staff = staff
        self.unixTimeStamp = unixTimeStamp #this makes comparing dates easier

    @staticmethod
    def create(animalID,sourcefile, staffList, foodList, feedingDate, feedingTime, unixTimeStamp):
      
      data = [['ID', 'Name', 'Manufacturer']]
      for s in foodList: data.append([s.foodID,s.foodName,s.manufacturer])
      print(AsciiTable(data).table)
      selection = input("Select a food by its ID: ")
      theFood = None

      while theFood is None:
        for food in foodList:
            if selection == food.foodID: theFood = food
        if theFood is None:
            print("This food doesn't exist in the database.")
            selection = input("Select a food by its ID: ")

      weight = input("Enter feeding weight: ")

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
      fo.write("\nI:%s,%s,%s,%s,%s,%s,%d" % 
                            (feedingDate,feedingTime,theFood.foodID,weight,theStaff.id,animalID, unixTimeStamp))
      print("Feeding report created for Animal-{} by Staff-{}".format(animalID, theStaff.id))
      fo.close()
      return Feeding(feedingDate, feedingTime, theFood, weight, theStaff, unixTimeStamp)