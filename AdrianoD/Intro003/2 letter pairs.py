import string
i = string.ascii_lowercase
j = list(map(str, i))
for x in j:
    for y in j:
        if x != y:
            print(x+y)

    
    
    
# print(j)
# for first in j:
#     for second in j:
#         pair = first + second
#         print(pair)
        
