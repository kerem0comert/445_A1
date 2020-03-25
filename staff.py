class Staff:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def printer(self):
        print("Name: " + self.name + "\nAge: " + str(self.age))