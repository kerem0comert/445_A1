class Environment:
    def __init__(self, humidity, size, temperature, h_of_light):
        self.humidity = humidity
        self.size = size
        self.temperature = temperature
        self.h_of_light = h_of_light

    @staticmethod
    def create(sourcefile):
        humidity = input("Enter Humidity: ")
        size = input("Enter Size: ")
        temperature = input("Enter Temperature: ")
        h_of_light = input("Enter Hours of light per day: ")
        fo=open(sourcefile,"a+")
        fo.write("\nE:%s,%s,%s,%s" % (humidity,size,temperature,h_of_light))
        fo.close()
        return Environment(humidity, size, temperature, h_of_light)