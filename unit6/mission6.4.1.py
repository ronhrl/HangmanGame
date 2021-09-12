def check_valid_input(letter_guessed, old_letter_guessed):
    if not letter_guessed.isalpha():
        return False
    elif len(letter_guessed) > 1:
        return False
    elif letter_guessed in old_letter_guessed:
        return False
    else:
        return True
