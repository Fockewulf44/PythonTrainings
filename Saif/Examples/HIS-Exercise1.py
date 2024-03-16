
# Exercise 1
# Find the longest word

sent1 = "Shrubberies are great places to find strawberries"

# def FindTheLongestWord(sentence):
#     longestWord=""
#     return longestWord
    
r1 = sent1.split(" ")
print(r1)

# word1 = (r1:1)
# word2 = (r1:2)
# word3 = (r1:3)

longestWord = ""
longestLength = 0

for v in r1:
    len(v)
    length=len(v)
    
    if length>longestLength:
        longestLength = length
        longestWord = v
        
print(longestWord)
print(longestLength)
    

# Algo
# 1. Split the sentence into words
# 2. In a loop check the length of each word
# 3. Return the longest word


