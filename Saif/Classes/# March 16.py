# March 16
# Classes

class User:
    username=""
    password=""
    title=""
    
    # def __ will show a list of functions
    def __init__(self, title, usr, pwd) -> None:
        self.title=title
        self.username = usr
        self.password = pwd
    
    def update_password(self, pwd):
        self.password = pwd
        
    def reset_password(self):
        self.password = ""
        



john_hopkins = User("John Hopkins", "CEO", "john1", "john2")

p = john_hopkins