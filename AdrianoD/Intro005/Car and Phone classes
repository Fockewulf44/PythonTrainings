class Car:


    def __init__(
        self, make: str, 
        model: str, 
        year: str, country: str, position: float, windows: bool
        ) -> None:
        
        self.make = make
        self.model = model
        self.year = year
        self.country = country
        self.position = position
        self.windows = windows

    def isForeign(self):
        if self.country == "US":
            return False
        else:
            return True

    def moveForward(self, distance):
        self.position += distance
        return self.position

    def moveBackward(self, distance):
        self.position -= distance
        return self.position
    
    def openWindows


hd = Car("Honda", "Accord", "2020", "Japan", 0)
fd = Car("Ford", "F-150", "2016", "US", 0)

print(hd.isForeign())
print(fd.moveForward(2.75), fd.moveBackward(.75))


class Phone:

    def __init__(self, passcode: str, profile: str, num: str) -> None:
        self.passcode = passcode
        self.profile = profile
        self.number = num

    def changeNumber(self, number):
        self.number = number

    def getProfile(self):
        return self.profile


iphone = Phone("12345", "John Appleseed", "295-193-1962")

iphone.changeNumber("194-624-6862")

print(iphone.number)
print(iphone.getProfile())
