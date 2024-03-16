# March 16
# Classes

class User:
    username=""
    password=""
    title=""
    
    def update_password(self, pwd):
        self.password = pwd
        
    def reset_password(self):
        self.password = ""
        