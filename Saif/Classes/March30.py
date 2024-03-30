# March30
# Write a program that takes a list of numbers and makes a new list of only the first and last elements of the given list. 
# For practice, write this code inside a function and inside use try/except

try:
    list = [5, 10, 15, 20, 25]


    first_number=list[0]
    print(first_number)
    
    last_index=len(list) - 1
    print(last_index)
    
    last_number=list[last_index]
    print(last_number)
    
    # calc_lastindex = len.list[-1]
    # print(calc_lastindex)
    newlist = []
    newlist.append(first_number)
    newlist.append(last_number)
    
    print(newlist)

except Exception as e:
    print(e.args)

# last_number=list[4]



# def first_number():
    
    
# def last_number():
    
    
# new_list = append first_number.last_number

# print(new_list)