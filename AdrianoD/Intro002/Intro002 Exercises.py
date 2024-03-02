# Print number of seconds in a year
seconds_in_min = 60
mins_in_hr = 60
hrs_in_day = 24
days_in_year = 365
sec_in_year = seconds_in_min * mins_in_hr * hrs_in_day * days_in_year
print(sec_in_year)

# Print the number of characters in a sentence
sentence = "I went to the market and got some groceries."
print(len(sentence))


# Create a function to calculate age.
def AgeCalc(dob: int):
    current_year = 2024
    age = current_year - dob
    return age


print(AgeCalc(2001))

# Create a function that returns the count of words in a sentence.


def WordCount(sentence2: str):
    wordlist = sentence2.split(" ")
    return len(wordlist)


sentence2 = "You are smart, you are loyal"
print(WordCount(sentence2))
