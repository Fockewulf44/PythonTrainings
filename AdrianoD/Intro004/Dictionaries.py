phonebook = {"Alice": "2341", "Beth": "9102", "Cecil": "3258"}
print(phonebook)
print(phonebook["Beth"])
print(phonebook.keys())

# Dictionary from list
list1 = [("name", "Gumby"), ("age", 42)]
d = dict(list1)
print(d)

# Conditionals, Loops, and other statements
tuple1 = ("name", "Gumby")
tuple2 = ("age", 42)
list2 = [tuple1, tuple2]
print(list2)

# if statement
list3 = [1, 2, 3, 4, 5, 6]
for num in list3:
    # print('num ' + str(num) + ' remainder: ' + str(num % 2))
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")

