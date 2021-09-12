import math


def squared_numbers(start, stop):
    list_of_squared = list()
    while start <= stop:
        list_of_squared.append(math.pow(start, 2))
        start += 1
    return list_of_squared
