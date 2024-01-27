colors = ['green', 'yellow', 'blue']

def quadratic(colors):
    for first in colors:
        for second in colors:
            print(first, second)

quadratic(colors)