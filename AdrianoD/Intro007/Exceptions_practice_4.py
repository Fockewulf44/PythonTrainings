# Write a program (function!) that takes a list and returns a new list that 
# contains all the elements of the first list minus all the duplicates.

# Extras:

# Write two different functions to do this - one using a loop and constructing a list, and another using sets.

list2 = [1, 1, 6, 3, 13, 3, 22, 2, 1]
newlist = []

try:
    list3 = set(list2)
    newlist1 = list(list3)
    print(newlist1)
except Exception as e:
    print(f"Error occurred: {e}")
finally:
    pass

try:
    print(sorted(set(list2)))
except Exception as e:
    print(f"Error occurred: {e}")
finally:
    pass


# print(dropDuplicates(list3))