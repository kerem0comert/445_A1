import re


class Staff:
    def __init__(self, id, fName, lName, office, tel):
        self.id = id
        self.fName = fName
        self.lName = lName
        self.office = office
        self.tel = tel

    @staticmethod
    def create(sourcefile):
        digitRegex = '\d{6}'
        officeRegex = '^A-(\d{3})$' #^ is the start of string and $ is end of string. They are used here
                                    #to signify an exact match. Otherwise A-123 would pass for instance,
                                    #as it contains A-123 which is a match.
        idInFileRegex =  'S:(\d+),' #this is used to search whether any input id exists in the text file
        fo=open(sourcefile,"a+")
        fo.seek(0) #without adding this line before reading, print returns \n rather than the 
                   #file contents. see https://stackoverflow.com/a/14639957/11330757
        foContents = fo.read()
        idList = re.findall(idInFileRegex,foContents)
    
        id = input("Enter ID (6 digits): ")
        while re.match(digitRegex, id) is None: 
            print("The format of the id is incorrect.")
            id = input("Enter ID (6 digits):")
        while id in idList:
            suggestion = int(idList[-1]) + 1
            print("{} is not unique as it already exists in the database. Suggestion: {}".format(
                id, suggestion))
            id = input("Enter ID (6 digits):")
       
        fName = input("Enter First Name: ")
        lName = input("Enter Last Name: ")
        
        office = input("Enter Office Number (A-XXX where X is digit):")
        while re.match(officeRegex, office) is None: 
            print("The format of the office number is incorrect.")
            office = input("Enter Office Number (A-XXX where X is digit):")

        tel = input("Enter Tel Number (6 digits):")
        while re.match(digitRegex, tel) is None: 
            print("The format of the telephone number is incorrect.")
            tel = input("Enter Tel Number (6 digits):")

        fo.write("\nS:%s,%s,%s,%s,%s" % (id,fName,lName,office,tel))
        fo.close()
        return Staff(id, fName, lName, office, tel)

  
        
