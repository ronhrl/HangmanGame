str_to_replace = input("Please enter a string: ")
char_to_replace = str_to_replace[0]

new_str = str_to_replace.replace(char_to_replace, 'e')
new_str_fix = new_str.replace('e', char_to_replace, 1)
print(new_str_fix)
