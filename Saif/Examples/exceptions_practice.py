list1 = [5, 7, 15, 0, 20]
smallnum = 20

for i in list1:
    
    try:
        for i in list1:
        print(smallnum/i)
        
    except ZeroDivisionError as z:
        print(Exception('!!Divided by Zero!!'))

finally:
    pass