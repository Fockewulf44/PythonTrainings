result = 0
integers = range(1, 1000)
for x in integers:
  if x % 3 == 0 or x % 5 == 0:
    result += x

print(result)