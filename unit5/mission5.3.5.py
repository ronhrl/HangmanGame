import math


def distance(num1, num2, num3):
    distance_num1_num2 = abs(num1 - num2)
    distance_num1_num3 = abs(num1 - num3)
    distance_num2_num3 = abs(num2 - num3)
    print(distance_num1_num2)
    print(distance_num1_num3)
    print(distance_num2_num3)
    if (distance_num1_num2 == 1 or distance_num1_num3 == 1) and (distance_num2_num3 >= 2 or
                                                                 distance_num1_num3 >= 2 or distance_num1_num2 >= 2):
        return True
    else:
        return False
