def choose_word(file_path, index):
    open_file = open(file_path, 'r')
    list_of_unique_words = list()
    list_of_all_words = list()
    count_of_words = 0
    #    lines_in_file = open_file.read()
    for line in open_file:
        for word in line.split(" "):
            count_of_words += 1
            list_of_all_words.append(word)
            if word not in list_of_unique_words:
                list_of_unique_words.append(word)
            else:
                continue
    # print(list_of_unique_words)
    num_different = len(list_of_unique_words)
    word_to_guess = list_of_all_words[(index - 1) % count_of_words]
    tuple_to_guess = (num_different, word_to_guess)
    return tuple_to_guess
