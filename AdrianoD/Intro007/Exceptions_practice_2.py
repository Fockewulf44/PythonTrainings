# Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only 
# the first and last elements of the given list. For practice, write this code inside a function and inside use try/except

a= [5,10,15,20,25]

def numFunction(num):
    newlist = []
    for i in num:
        try:
            newlist.append(num[0])
            newlist.append(num[-1])
        except Exception as e:
            print(f"Error occurred: {e}")
        finally:
            return newlist

print(numFunction(a))
