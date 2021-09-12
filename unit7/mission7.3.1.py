def show_hidden_words(secret_word, old_letters_guessed):
    i = 0
    str_to_guess = ""
    while i < len(secret_word):
        j = 0
        while j < len(old_letters_guessed):
            if secret_word[i] == old_letters_guessed[j]:
                str_to_guess += old_letters_guessed[j]
                j += 1
                break
            j += 1
            if j == len(old_letters_guessed):
                str_to_guess += " _ "
                break
        i += 1
    return str_to_guess
