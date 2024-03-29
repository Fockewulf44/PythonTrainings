list1 = [5, 7, 15, 0, 20]
smallnum = 20



for i in list1:
    try:
        print(smallnum/i)
    except ZeroDivisionError as z:
        print(Exception('!!Divide by zero!!'))
    finally:
        pass


