# Classes: 
# 1: Car. Add variables like model, year,etc. Add functions like move forward, move back, open widnows, etc
# 2. Mobile Phone. Same here. Create properties and functions
# and for each class use Init function to initialize some values

class car:
    model=""
    year=""
    mileage=""
    
    def __init__(self, model, year, mileage) -> None:
        self.model=model
        self.year=year
        self.mileage=mileage
    
    def moveforward():
        print("Moving forward")
    
    def moveback():
        print("Moving backwards")
    
    def openwindows():
        print("Open Windows")

bmw = car("M5CSL", "2024", "30000")

class phone:
    brand=""
    storage=""
    os=""
    
    def __init__(self, brand, storage, os) -> None:
        self.brand=brand
        self.storage=storage
        self.os=os
        
samsung = phone("S24 Ultra", "512gb", "Android")