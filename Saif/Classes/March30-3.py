# March 30 Exercise 3

# Write a program (function!) that takes a list and returns a new list that 
# contains all the elements of the first list minus all the duplicates.

try:
    list1=[1, 5, 5, 10, 10, 100, 200, 300]
    
    
    # last_index=len(list)-1
    # print(last_index)
    
    # print(list1)
    
    unique = list(set(list1))
    
    print(unique)
            
except Exception as e:
    print(e.args)
