# March 30th - 2nd exercise

# Take a list, say for example this one: a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# and write a program that prints out all the elements of the list that are less than 5.
# Extras: Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list.

try:
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

    last_index=len(a) - 1
    print(last_index)

    newlist=[]
    over5=[]
    under5=[]

    for x in a:
        if x<5:
            print(x)
            newlist.append(x)

    print(newlist)

except Exception as e:
    print(e.args)
    