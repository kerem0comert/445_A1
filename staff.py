class Staff:
    def __init__(self, id, fName, lName, office, tel):
        self.id = id
        self.fName = fName
        self.lName = lName
        self.office = office
        self.tel = tel

    @staticmethod
    def create():
        id = input("Enter ID: ")
        fName = input("Enter First Name: ")
        lName = input("Enter Last Name: ")
        office = input("Enter Office Number:")
        tel = input("Enter Tel Number:")
        return Staff(id, fName, lName, office, tel)

  
        
