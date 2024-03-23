# Exceptions
# Try/except/finally

# try:
#     result = 'hello world'/2
# except ZeroDivisionError:
#     print('Division by zero')
# except Exception as e:
#     print('Generic exception.')
# finally:
#     pass

d1 = {1: "San Francisco", 2: "Karachi", 3: "Baku"}

if d1.get(2) == None:
    raise Exception("There is no key 2")
else:
    print(d1[2])

if d1.get(5) == None:
    raise Exception("There is no key 5")
else:
    print(d1[5])

# try:
#     print(f"Value of key 1 is {d1[1]}")
#     print(f"Value of key 5 is {d1[5]}")
# except ZeroDivisionError:
#     print("Division by zero")
# except Exception as e:
#     print("The following error has occurred:")
#     print(f"Error type  is {type(e)}, and the message is {e.args}.")
# finally:
#     pass

# bignumber = 200
# list1 = [4, 1, 10, 0, 8]

# try:
#     for i in list1:
#         print(bignumber/i)
# except Exception as e:
#     print(e.args)


# for i in list1:
#     print(bignumber/i)
