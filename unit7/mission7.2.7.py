def arrow(my_char, max_length):
    i = 1
    while i <= max_length:
        print(my_char * i)
        i += 1
    i -= 2
    while i > 0:
        print(my_char * i)
        i -= 1
