class Food:
    def __init__(self, foodName, manufacturer):
        self.foodName = foodName
        self.manufacturer = manufacturer

    @staticmethod
    def create():
        foodName = input("Enter Food Name: ")
        manufacturer = input("Enter Manufacturer: ")
        return Food(foodName, manufacturer)