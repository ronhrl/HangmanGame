def check_win(secret_word, old_letters_guessed):
    i = 0
    count_of_correct = 0
    while i < len(secret_word):
        j = 0
        while j < len(old_letters_guessed):
            if secret_word[i] == old_letters_guessed[j]:
                count_of_correct += 1
                j += 1
                break
            j += 1
        i += 1
    if count_of_correct == len(secret_word):
        return True
    else:
        return False
