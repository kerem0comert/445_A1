class Food:
    def __init__(self, foodName, manufacturer):
        self.foodName = foodName
        self.manufacturer = manufacturer

    @staticmethod
    def create(sourcefile):
        foodName = input("Enter Food Name: ")
        manufacturer = input("Enter Manufacturer: ")
        fo=open(sourcefile,"a+")
        fo.write("\nF:%s,%s" % (foodName,manufacturer))
        fo.close()
        return Food(foodName, manufacturer)