# March 9 Bootcamp

# website = "https://google.com"

# website [-3:] = "org"

# print(website)
# result = TypeError: 'str' object does not support item assignment

# format = "Hello, %s. %s enough for ya"
# values = ("world", "Hot")
# print(format % values)
# # returns: "Hello, world. Hot enough for ya" i.e. %s is used whenever you have key words (world, Hot)


# Page 46

# result = "{}, {}, and {}".format('first','second','third')
# print(result)
# .format is applied in front of a string to replace values in curly brackets with those in .format, moving in order

# f-string = formatted strings
# import math
# print(
#     f'The value of pie is approximately {math.pi:.3f}.'
#     )
# # returns The value of pie is approximately 3.142.

# animals = 'eels'
# animals2 = 'cats'
# print(f'My hovercraft is full of {animals} and {animals2}.')
# # returns "My hovercraft is full of eels and cats."
# if you remove f early, it'll return My hovercraft is full of {animals} and {animals2}.

#Moving to Chapter #4 - Dictionary Pg60
# Dictionaries have key:value
# phonebook = {'Alice': '2341', 'Beth':'9102', 'Cecil': '3258'}
# print(phonebook)
# returns {'Alice': '2341', 'Beth': '9102', 'Cecil': '3258'}

# phonebook = {'Alice': '2341', 'Beth':'9102', 'Cecil': '3258'}
# print(phonebook['Alice'])
# returns Alice's value = 2341

# phonebook = {'Alice': '2341', 'Beth':'9102', 'Cecil': '3258'}
# print(phonebook['2341'])
# # returns an error: KeyError: '2341'

# # To get the key, use .keys:
# phonebook = {'Alice': '2341', 'Beth':'9102', 'Cecil': '3258'}
# print(phonebook.keys())
# # returns dict_keys(['Alice', 'Beth', 'Cecil'])

# # Dictionary from List:
# list1 =[("name", "Gumby"), ("age", 42)]
# d = dict(list1)
# print(d)
# # returns {'name': 'Gumby', 'age': 42}

# items =[("name", "Gumby"), ("age", 42)]
# d = dict(items)
# print (d)
# returns {'name': 'Gumby', 'age': 42}

# Page71 - Chapter 5: Conditions, loops, if-statements
# Tuple example - Tuples are immutable and can't be changed, so different from lists

# list1 = [("name", "Gumby"), ("age", 42)]
# d = dict(list1)
# print(d)
# # returns {'name': 'Gumby', 'age': 42} because d variable has converted the list to a dictionary


# # Conditions, loops, and other statements
# tuple1 = ('name', 'Gumby')
# tuple2 = ('age', 42)
# list2 = [tuple1, tuple2]
# print(list2)
# # returns [('name', 'Gumby'), ('age', 42)]

# tuples can be turned into lists; and lists can be turned into dictionaries
# tuples are data structures, like lists

# Page42:
# Tuples are immutable sequences ie they can't be changed; usually written in parantheses. you can have empty tuples()

# x = 1, 2, 3
# print(x[0:2])
# returns (1, 2) = made it a tuple

# x = 1, 2, 3
# print(x[0:3]) # 0 = start from position 1; include 3 values from position 1)
# # returns (1, 2, 3)

# Conditional loops & other statements
# if statement
# list3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for num in list3:
#     if num % 2 == 0:
#         print(num)
        
# returns: 
# 2
# 4
# 6
# 8
# 10



# list3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for num in list3:
#     if num % 2 == 0:      # The '% 2' modulus prints even for numbers divisible by two without returning a decimal = Floor division
#         print("Even")
#     else:
#         print("Odd")

# # returns:
# # Odd
# # Even
# # Odd
# # Even
# # Odd
# # Even
# # Odd
# # Even
# # Odd
# # Even


# list3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for num in list3:
#     print('num ' + str(num) +' remainder:' + str(num % 2))
# # returns:
# # num 1 remainder:1
# # num 2 remainder:0
# # num 3 remainder:1
# # num 4 remainder:0
# # num 5 remainder:1
# # num 6 remainder:0
# # num 7 remainder:1
# # num 8 remainder:0
# # num 9 remainder:1
# # num 10 remainder:0

