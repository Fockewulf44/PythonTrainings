### Simple arithmetic ###

result = "Hello, " + "Class..."
print(result)

result2 = 3.25 + 6.75
print(result2)

result3 = 62 + 90
print(result3)

# Adding lists together
list1 = [1, 3, 5]
list2 = [7, 9, 11]
list3 = list1 + list2
print(list3)

# Floor division '//' rounds the remainder DOWN to the nearest whole number
result4 = result3 // 2.5
print(result4)

# For loop + Modulo, appending to new list
# Note: 'i' refers to the index (the name 'i' is arbitrary)
newlist = []
listex = [1, 2, 3, 4, 5, 6]
for i in listex:
    if i % 2 == 0:
        newlist.append(i)

print(newlist)
