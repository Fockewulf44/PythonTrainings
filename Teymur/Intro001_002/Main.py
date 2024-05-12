#Intro 001
# Integer
# 1,2,3,4,100,200 128000000
# Float (floating pointer number)
# 10.5; 100.3; 50.20

import math as m

x1 = 100
y1 = 50

z1 = 10 % 3
# print(z1)

s1 = "My name "
s2 = " is John"
s5 = "20.5"

s3 = str(x1) + s2

s11 = float(s5)
s12 = s11 + 100

# Intr0_002
# List
months = ["January", "February", "March", "December", "July"]

m_sorted = sorted(months)

# print(m_sorted)
# Append
months.append("June")
months.insert(2,"October")

# print(months)
# index              0    1   2  3   4   5
week_temperatures = [70, 65, 62, 66, 68, 80]
week_temperatures.append(100)

months.append(200)
# print(months)

for m in months:
    print(m)

    

# Sort
# sorted_w_t = sorted(week_temperatures)

# Slices
slice1 = week_temperatures[1:5]
# print(slice1)


# Tuple
t1 = (20, 40 , 10)

list_t1 = list(t1)

# print(t1)
# print(list_t1)
list_t1.append(20000)
# print(list_t1)


def CalcCoordinates():
    # some logic
    x = 100
    y = 200
    z = 333
        
    return (x,y,z)


