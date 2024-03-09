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
