guess_char = input("Please enter a word: ")

if len(guess_char) > 1 and not guess_char.isalpha():
    print("E3")

elif not guess_char.isalpha():
    print("E2")

elif len(guess_char) > 1:
    print("E1")

else:
    print(guess_char.lower())
