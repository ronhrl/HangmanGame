def is_greater(my_list, n):
    list_of_bigger = list()
    for num in my_list:
        if num > n:
            list_of_bigger.append(num)
    return list_of_bigger
