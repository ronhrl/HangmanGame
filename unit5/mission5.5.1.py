def is_valid_input(letter_guessed):
    if not letter_guessed.isalpha():
        return False
    elif len(letter_guessed) > 1:
        return False
    else:
        return True
