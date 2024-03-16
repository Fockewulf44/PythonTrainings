# HIS "longest word" example
sentence = "I am learning Python and SQL on Saturday's at Lighthouses Mosque"
longestword = ""
list1=sentence.split(" ")
print(list1)

for i in list1:
    if len(i) > len(longestword):
        longestword = i
print(longestword)