class Food:
    def __init__(self, foodID, foodName, manufacturer):
        self.foodID = foodID
        self.foodName = foodName
        self.manufacturer = manufacturer

    @staticmethod
    def create(sourcefile, foodList):
        No=1
        for x in foodList: No += 1
        foodID = str(No)
        foodName = input("Enter Food Name: ")
        manufacturer = input("Enter Manufacturer: ")
        fo=open(sourcefile,"a+")
        fo.write("\nF:%s,%s,%s" % (foodID,foodName,manufacturer))
        fo.close()
        return Food(foodID, foodName, manufacturer)