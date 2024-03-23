# Exceptions
# try/except/finally

d1 = {1:"San-Franciso", 2:"Karachi", 3:"Baku"}


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
#     print("The following error has occured:")
#     print(f"Error type is {type(e)}, and the message is {e.args}")
# finally:
#     pass





