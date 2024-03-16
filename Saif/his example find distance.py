# HIS Distance example: Find the distance between the two furthest apart values in a list.

list1 = [9, 6, 3, 5, 15, 4, 7]
highest = 0
lowest = 1000

for i in list1:
    if i > highest:
        highest = i
    elif i < lowest:
        lowest = i
print(highest - lowest)

# 15 - 3