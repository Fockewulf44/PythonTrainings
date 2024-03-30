# Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only 
# the first and last elements of the given list. For practice, write this code inside a function and inside use try/except

a= [5,10,15,20,25]

def numFunction(num):
    newlist = []
    try:
        newlist.append(num[0])
        newlist.append(num[-1])
    except Exception as e:
        print(f"Error occurred: {e}")
    finally:
        return newlist
    
    

print(numFunction(a))

# Alternate method

list2 = [2,4,6,8,10,12]

def numFunction2(num):
    list3 = []
    try:
        last_index = num[len(num) - 1]
        first_index = num[0]
        list3 = [first_index, last_index]
    except Exception as e:
        print(f"Error occurred: {e}")
    finally:
        return list3
        
print(numFunction2(list2))
        
    


