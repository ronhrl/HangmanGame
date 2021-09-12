def seven_boom(end_number):
    numbers = range(0, end_number, 1)
    list_of_numbers = list()
    for num in numbers:
        if num % 7 == 0 or num % 10 == 7:
            list_of_numbers.append("BOOM")
        else:
            list_of_numbers.append(num)
    return list_of_numbers
