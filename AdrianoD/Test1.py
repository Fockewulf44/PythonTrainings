def dist(points):
    lowest = points[0]
    highest = -1000
    for i in points:
        if i > highest:
            highest = i
        if i < lowest:
            lowest = i
    result = highest - lowest
    return result


list1 = [-1, -2, -3]
print(dist(list1))
