input_word = input("Please enter a string: ")

small_case = input_word[0: len(input_word) // 2: 1].lower()
big_case = input_word[len(input_word) // 2:: 1].upper()

small_big_word = small_case + big_case

print(small_big_word)
