from terminaltables import ascii_table

class Staff:
    def __init__(self, id, fName, lName, office, tel):
        self.id = id
        self.fName = fName
        self.lName = lName
        self.office = office
        self.tel = tel
    def printer(self):
        print('Name:{}\nSurname:{}!'.format(self.fName, self.lName)) 
