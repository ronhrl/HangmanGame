def numbers_letters_count(my_str):
    num_of_digits = 0
    num_of_chars = 0
    list_of_dig_char = list()
    for ch in my_str:
        if ch.isdigit():
            num_of_digits += 1
    num_of_chars = len(my_str) - num_of_digits
    list_of_dig_char.append(num_of_digits)
    list_of_dig_char.append(num_of_chars)
    return list_of_dig_char
