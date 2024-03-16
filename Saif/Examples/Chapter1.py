# If you are familiar with other computer languages, you may be used to terminating every line with asemicolon. 
# There is no need to do so in Python. A line is a line, more or less. You may add a semicolon if you like, but 
# it won’t have any effect (unless more code follows on the same line), and it is not a common thing to do.

# print("Hello, world!")

# help() for python modules, keywords, symbols, or topics. 

# Algorithms consist of a series of instructions to be followed in order. Some of the instructions may be done directly (“take some SPAM”), while some require
# some deliberation (“If a particularly spicy SPAM is desired”), and others must be repeated several times (“Check every 10 minutes.”)

# Recipes and algorithms consist of ingredients (objects, things) and instructions (statements). In this
# example, SPAM and eggs are the ingredients, while the instructions consist of adding SPAM, cooking for a
# given length of time, and so on.

# All the usual arithmetic operators work as expected. Division produces decimal numbers, called floats (or floating-point numbers).
# If you’d rather discard the fractional part and do integer division, you can use a double slash. 
# e.g. 1 // 2 ==> 0, and 1 // 1 ==> 1, and 5.0 // 2.4 ==> 2.0

# Now you’ve seen the basic arithmetic operators (addition, subtraction, multiplication, and division),
# but I’ve left out a close relative of integer division.
# e.g. 1 % 2 ==> 1
# This is the remainder (modulus) operator. x % y gives the remainder of x divided by y. In other words, it’s
# the part that’s left over when you use integer division. That is, x % y is the same as x - ((x // y) * y).
# e.g. 10 // 3 ==> 3; 10 % 3 ==> 1; 9 // 3 ==> 3; 9 % 3 ==> 0; 2.75 // 0.5 ==>  5; 2.75 % 0.5 ==> 0.25
# Here 10 // 3 is 3 because the result is rounded down. But 3 × 3 is 9, so you get a remainder of 1. When you
# divide 9 by 3, the result is exactly 3, with no rounding. Therefore, the remainder is 0. This may be useful
# if you want to check something “every 10 minutes” as in the recipe earlier in the chapter. You can simply
# check whether minute % 10 is 0.

# the remainder operator works just
# fine with floats as well. It even works with negative numbers, and this can be a little confusing.
# e.g. 10 % 3 ==> 3
# 10 % -3 ==> -2
# -10 % 3 ==> 2
# -10 % -3 ==> -1
# Looking at these examples, it might not be immediately obvious how it works. It’s probably easier to
# understand if you look at the companion operation of integer division.
# e.g. 10 // 3 ==> 3
# 10 // -3 ==> -4
# -10 // 3 ==> -4
# -10 // -3 ==> 3

# Given how the division works, it’s not that hard to understand what the remainder must be. The important
# thing to understand about integer division is that it is rounded down, which for negative numbers is away
# from zero. That means -10 // 3 is rounded down to -4, not up to -3.

# Exponentiation (or power) operator:
# 2 ** 3 ==> 8; -3 ** 2 ==> -9; (-3) ** 2 ==> 9
# Note that the exponentiation operator binds tighter than the negation (unary minus), so -3**2 is in fact the
# same as -(3**2). If you want to calculate (-3)**2, you must say so explicitly.

# Hexadecimals Octals and Binary
# Hexadecimal, octal, and binary numbers are written like this:
# 0xAF ==> 175; 010 ==> 8; 0b1011010010 ==> 772
# The first digit in both of these is zero.

# Variables
# A variable is a name that represents (or refers to) some value. For
# example, you might want the name x to represent 3. To make it so, simply execute the following: x = 3
# This is called an assignment. We assign the value 3 to the variable x. Another way of putting this is to say that
# we bind the variable x to the value (or object) 3. After you’ve assigned a value to a variable, you can use the
# variable in expressions: x * 2 ==> 6
# Unlike some other languages, you can’t use a variable before you bind it to something. There is no “default
# value.”

# Names, or identifiers, in Python consist of letters, digits, and underscore
# characters (_). They can’t begin with a digit, so Plan9 is a valid variable name, whereas 9Plan is not.

# Statements = instructions
# What’s the difference between a statement and an expression? You could think of it like this: an
# expression is something, while a statement does something. For example, 2 * 2 is 4, whereas print(2 * 2)
# prints 4. The two behave quite similarly, so the difference between them might not be all that clear.
# 2 * 2 ==> 4; print(2*2) ==> 4
# Actually, print is a function (more on those later in the chapter), so what I’m referring to as a
# print statement is simply a function call.

# The difference between statements and expressions is more obvious when dealing with assignments.
# Because they are not expressions, they have no values that can be printed out by the interactive interpreter.
# x = 3 ==> (prompt)
# You simply get a new prompt immediately. Something has changed, however. We now have a new variable
# x, which is now bound to the value 3. To some extent, this is a defining quality of statements in general: they
# change things. For example, assignments change variables, and print statements change how your screen
# looks.

# Assignments are probably the most important type of statement in any programming language,
# although it may be difficult to grasp their importance right now. Variables may just seem like temporary
# “storage” (like the pots and pans of a cooking recipe), but the real power of variables is that you don’t need to
# know what values they hold in order to manipulate them.5
# For example, you know that x * y evaluates to the product of x and y, even though you may have
# no knowledge of what x and y are. So, you may write programs that use variables in various ways without
# knowing the values they will eventually hold (or refer to) when the program is run.

# Getting Input from the User
# You’ve seen that you can write programs with variables without knowing their values. Of course, the
# interpreter must know the values eventually. So how can it be that we don’t? The interpreter knows only
# what we tell it, right? Not necessarily.
# You may have written a program, and someone else may use it. You cannot predict what values users
# will supply to the program. Let’s take a look at the useful function input.

# >>> input("The meaning of life: ")
# The meaning of life: 42
# '42'
# What happens here is that the first line (input(...)) is executed in the interactive interpreter. It prints out
# the string "The meaning of life: " as a new prompt. I type 42 and press Enter. The resulting value of
# input is that very number (as a piece of text, or string), which is automatically printed out in the last line.
# # Converting the strings to integers using int, we can construct a slightly more interesting example:
# >>> x = input("x: ")
# x: 34
# >>> y = input("y: ")
# y: 42
# >>> print(int(x) * int(y))
# 1428
# Here, the statements at the Python prompts (>>>) could be part of a finished program, and the values entered
# (34 and 42) would be supplied by some user. Your program would then print out the value 1428, which is the
# product of the two. And you didn’t have to know these values when you wrote the program, right?

# >>> x = input("x: ")
# x: 34
# >>> y = input("y: ")
# y: 42
# >>> print(int(x) * int(y))
# 1428
# Here, the statements at the Python prompts (>>>) could be part of a finished program, and the values entered
# (34 and 42) would be supplied by some user. Your program would then print out the value 1428, which is the
# product of the two.

# The IF statement
# The if statement lets you perform an action (another
# statement) if a given condition is true. One type of condition is an equality test, using the equality
# operator, ==. Yes, it’s a double equality sign. (The single one is used for assignments, remember?)
# You put this condition after the word if and then separate it from the following statement with a colon.
# >>> if 1 == 2: print('One equals two')
# ...
# >>> if 1 == 1: print('One equals one')
# ...
# One equals one
# >>>
# Nothing happens when the condition is false. When it is true, however, the statement following the colon
# (in this case, a print statement) is executed. Note also that when using if statements in the interactive
# interpreter, you need to press Enter twice before it is executed. 

# So, if the variable time is bound to the current time in minutes, you could check whether you’re “on the
# hour” with the following statement:
# if time % 60 == 0: print('On the hour!')

# Functions
# In the “Numbers and Expressions” section, I used the exponentiation operator (**) to calculate powers. The
# fact is that you can use a function instead, called pow.
# >>> 2 ** 3
# 8
# >>> pow(2, 3)
# 8
# A function is like a little program that you can use to perform a specific action. Python has a lot of functions
# that can do many wonderful things. In fact, you can make your own functions, too (more about that later);
# therefore, we often refer to standard functions such as pow as built-in functions.

# Using a function as I did in the preceding example is called calling the function. You supply it with
# arguments (in this case, 2 and 3), and it returns a value to you. Because it returns a value, a function call is
# simply another type of expression, like the arithmetic expressions discussed earlier in this chapter.6 In fact, you
# can combine function calls and operators to create more complicated expressions.
# 6Function calls can also be used as statements if you simply ignore the return value.

# >>> 10 + pow(2, 3 * 5) / 3.0
# 10932.666666666666
# Several built-in functions can be used in numeric expressions like this. For example, abs gives the absolute
# value of a number, and round rounds floating-point numbers to the nearest integer.
# >>> abs(-10)
# 10
# >>> 2 // 3
# 0
# >>> round(2 / 3)
# 1.0
# Notice the difference between the two last expressions. Integer division always rounds down, whereas round
# rounds to the nearest integer, with ties rounded toward the even number. But what if you want to round a
# given number down? For example, you might know that a person is 32.9 years old, but you would like to
# round that down to 32 because she isn’t really 33 yet. Python has a function for this (called floor)—it just
# isn’t available directly. As is the case with many useful functions, it is found in a module.

# Modules
# You may think of modules as extensions that can be imported into Python to expand its capabilities. You
# import modules with a special command called (naturally enough) import. The function mentioned in the
# previous section, floor, is in a module called math.
# >>> import math
# >>> math.floor(32.9)
# 32
# Notice how this works: we import a module with import and then use the functions from that module by
# writing module.function. For this operation in particular, you could actually just convert the number into an
# integer, like I did earlier, with the results from input.
# >>> int(32.9)
# 32
# Similar functions exist to convert to other types (for example, str and float). In fact, these aren’t
# really functions—they’re classes.
# The math module has several other useful functions, though. For example, the opposite of floor is ceil
# (short for “ceiling”), which finds the smallest integral value larger than or equal to the given number.
# >>> math.ceil(32.3)
# 33
# >>> math.ceil(32)
# 32

# If you are sure that you won’t import more than one function with a given name (from different modules),
# you might not want to write the module name each time you call the function. Then you can use a variant of
# the import command.
# >>> from math import sqrt
# >>> sqrt(9)
# 3.0
# After using the from module import function, you can use the function without its module prefix

