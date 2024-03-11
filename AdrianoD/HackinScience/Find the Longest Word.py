# Find the Longest Word

sent1 = 'Shrubberies are great'

def FindTheLongestWord(sentence):
    longestword = ''
    longestlength = 0
    list1 = sentence.split()
    for i in list1:
        if len(i) > longestlength:
            longestlength = len(i)
            longestword = i
    return longestword 

print(FindTheLongestWord(sent1))

FLAVORS = [
    "Banana",
    "Chocolate",
    "Lemon",
    "Pistachio",
    "Raspberry",
    "Strawberry",
    "Vanilla",
]

x = 0
y = 0

while x < len(FLAVORS):
    y = x + 1
    while y < len(FLAVORS):
        # list1.append(FLAVORS[x] + ',' + FLAVORS[y])
        print(FLAVORS[x] + ', ' + FLAVORS[y])
        y += 1
    x += 1 
    
    

    