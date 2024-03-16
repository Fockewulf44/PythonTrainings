
# #page60
# phonebook = {
#     'Alice':'2341',
#     'Beth':'2303',
#     'Cecil':'3258'}
# print(phonebook['Alice'])
# print(phonebook)
# print(phonebook.keys())

# #Dictionary from list
# list1 = [("name", "Gumby"), ("age", 42)]
# d = dict(list1)
# print(d)

# #Conditional, Loops, and other statements (tuple- immutable sequence) p.42
# tuple1 = ('name', 'Gumby')
# tuple2 = ('age', 42)
# list2 = [tuple1, tuple2]
# print(list2)

# # if statement %-magulus 2/2= the reminder is 0 it means it is even. remainder it means it feel be not a whole number when divided
# list3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for num in list3:
#     print('num'+ str(num) + ' remainder: ' + str(num%2))
#     if num % 2 == 0:
#         print("Even")
#     else:
#         print("Odd")

# numbers = list(range(0, 10))
# squared_numbers = []
# for number in numbers:
#     squared_number = number * number
#     squared_numbers.append(squared_number)

# for num in range(0, 10):
#     print(num**2)

# # Print the squared numbers
# print(squared_numbers)


list10 =[5, 10, 44, 11, 22]
biggestnum = 0
for num in list10:
    if num>biggestnum:
        biggestnum=num
print(biggestnum)

#find the longest word in the sentence
text = 'My lovely sentence, I am making it longer'
x = len(text)
print(x)