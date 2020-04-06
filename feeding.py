import datetime
from terminaltables import AsciiTable

class Feeding:
    def __init__(self, date, time, food, weight, staff):
        self.date = date
        self.time = time
        self.food = food
        self.weight = weight
        self.staff = staff

    @staticmethod
    def create(animalID,sourcefile, staffList, foodList):
      feedingDate = datetime.datetime.today().strftime("%d/%m/%Y")
      feedingTime = datetime.datetime.now().strftime("%H:%M")
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
      fo.write("\nI:%s,%s,%s,%s,%s,%s" % (feedingDate,feedingTime,theFood.foodID,weight,theStaff.id,animalID))
      fo.close()
      return Feeding(feedingDate, feedingTime, theFood, weight, theStaff)