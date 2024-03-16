# result = 100*9
# text1 = "This is some text"
# list1 = ["USA", "Pakistan", "Russia", "Kongo"]
# listofnumbers = [1,2,3,4,5,6,7,8,9]
# list1.append("Indonesia")
# list1.sort()
# print(list1)
# print(result)
# print(text1)
# print(listofnumbers)

# dict1 = {"1":"USA", "2":"Russia", "3":"Indonesia"}
# print("If there is a key 6:" + str(dict1.get("6")))

# print(dict1["1"])
# print(dict1["2"])

# print(2*36)
# print(1+2*3.)
# print(1/2)
# print((2+2)*3)
# print(2+7)
# list1 = [1,2,3,4,5,6,7,8,9]
# print(list1)
# list1.append(10)
# print(list1)
# dict1={1:"America", 2:"Pakistan", 3:"Russia", 4:"India"}
# print(dict1)
# print(dict1[2])
# # You can only search dictionaries by value, not key

# result=dict1.get(3)
# print(result)

# print(2*2)
# print(100/4)
# print(100/55)
# print(1000*2+50)
# print((100*200)+3000)

# listofnumbers=[100, 200, 300, 400, 500, 600, 700, 800]
# listofcountries=["USA", "Pakistan", "India", "Russia", "Japan", "France"]
# print(listofnumbers)

# listofnumbers.append(1000)
# listofnumbers.append(10000)

# print(listofnumbers)

# listofcountries.append(100)
# print(listofcountries)

# listofcountries.append("Italy")
# print(listofcountries)

# # Classes:

# import datetime as dt

# class A:
#     title="Class A"
#     name="Some specific name"
    
    
#     def getmytitle(self):
#         return self.title
    
#     def getmyname(self):
#         return self.name
    

# class B(A):
#     def getTodaysDate(self):
#         return dt.datetime.today()

# # v = A()

# v1 = B()


# # print(v.getmytitle())
# # print(v.getmyname())
# print(v1.getTodaysDate())

# print(v1.getmytitle())

class User:
    name = ""
    pw = ""
    def setUserlName(self, name):
        self.name = name
    def setPassword(self, pw):
        self.pw = pw
        
class MacUser(User):
    status = False
    on = False
    def TurnOn(self, status):
        return status
    
    John = User()
    John.name = "John55"
    John.pw = "examplePW"
    
    print(John.name)
    print(John.pw)
    
    
    