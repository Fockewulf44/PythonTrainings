# Basic String Operations
format = "Hello, %s, %s enough for ya"
values = ("world", "Hot")
print(format % values)

result = "{}, {} and {}".format("first", "second", "third")
print(result)

# f strings
import math
print(f"The value of pi is approximately {math.pi:.3f}.")

from math import e
print(f"Euler's constant is roughly {e}")

animals = "eels"
animals2 = "cats"
print(f"My hovercraft is full of {animals} and {animals2}.")


