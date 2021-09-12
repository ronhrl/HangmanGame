def last_early(my_str):
    last_char = my_str[-1]
    str_length = len(my_str)
    print(str_length)
    print(last_char)
    if last_char in my_str:
        return True
    else:
        return False

