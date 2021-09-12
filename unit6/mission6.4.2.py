def check_valid_input(letter_guessed, old_letter_guessed):
    lower = letter_guessed.lower()
    if not letter_guessed.isalpha():
        return False
    elif len(letter_guessed) > 1:
        return False
    elif lower in old_letter_guessed:
        return False
    else:
        return True


def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    is_valid = check_valid_input(letter_guessed, old_letters_guessed)
    if is_valid:
        old_letters_guessed.append(letter_guessed)
        return True
    else:
        print("X")
        old_letters_guessed.sort()
        arrow = "->"
        print_string_arrows = arrow.join(old_letters_guessed)
        print(print_string_arrows)
        return False
