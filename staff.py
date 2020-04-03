class Staff:
    def __init__(self, id, fName, lName, office, tel):
        self.id = id
        self.fName = fName
        self.lName = lName
        self.office = office
        self.tel = tel

    @staticmethod
    def create(sourcefile):
        id = input("Enter ID: ")
        fName = input("Enter First Name: ")
        lName = input("Enter Last Name: ")
        office = input("Enter Office Number:")
        tel = input("Enter Tel Number:")
        fo=open(sourcefile,"a+")
        fo.write("\nS:%s,%s,%s,%s,%s" % (id,fName,lName,office,tel))
        fo.close()
        return Staff(id, fName, lName, office, tel)

  
        
