class Environment:
    def __init__(self, humidity, size, temperature, h_of_light,environmentID):
        self.humidity = humidity
        self.size = size
        self.temperature = temperature
        self.h_of_light = h_of_light
        self.environmentID = environmentID

    @staticmethod
    def create(sourcefile,environmentList):
        humidity = input("Enter Humidity: ")
        size = input("Enter Size: ")
        temperature = input("Enter Temperature: ")
        h_of_light = input("Enter Hours of light per day: ")
        No=1
        for x in environmentList:No += 1
        environmentID = No
        fo=open(sourcefile,"a+")
        fo.write("\nE:%s,%s,%s,%s,%s" % (humidity,size,temperature,h_of_light,environmentID))
        fo.close()
        return Environment(humidity, size, temperature, h_of_light,environmentID)