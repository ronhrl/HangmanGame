def count_chars(my_str):
    dict_chars_count = {}
    for char in my_str:
        if char == " ":
            continue
        num_of_times = my_str.count(char)
        dict_chars_count[char] = num_of_times
    return dict_chars_count
