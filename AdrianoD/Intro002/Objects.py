class User:
    username = ""
    password = ""
    title = ""

    def __init__(self, title, usr, pwd) -> None:
        self.title = title
        self.username = usr
        self.password = pwd
        title = "Product Manager"

    def update_password(self, pwd):
        self.password = pwd

    def reset_password(self):
        self.password = ""


john_hopkins = User("CEO", "CEO1", "1234")

p = john_hopkins
print(p.username)
