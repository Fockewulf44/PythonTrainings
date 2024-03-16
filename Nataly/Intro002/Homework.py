 #Print number of seconds in a year
days=365
hours=24
minutes=60
seconds=60
print("number of seconds in a year:", days*hours*minutes*seconds)
#answer number of seconds in a year: 31536000


# Create a function to calculate age.
birthyear=1985
currentyear=2024
print("my current age:", currentyear-birthyear)
 #answer my current age: 39

def Myage(dob: int):
    currentyear = 2024
    age = currentyear - dob
    return(age)
print(Myage(1985))

# Create a function that returns the count of words in a sentence.


def WordCount(mysentence: str):
    wordlist = mysentence.split(" ")
    return len(wordlist)


mysentence = "Is Python a snake?"
print(WordCount(mysentence))