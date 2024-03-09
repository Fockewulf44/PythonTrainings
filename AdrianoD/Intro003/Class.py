class User:
    name = ""
    pw = ""

    def setUserName(self, name):
        self.name = name

    def setPassWord(self, pw):
        self.pw = pw


class MacUser(User):
    status = False
    on = False

    def TurnOn(self, status):
        return status


John = User()
John.name = "John55"
John.pw = "example1234"

example = MacUser()
example.status = True
print(example.status)
