user_digits = input("Enter three digits (each digit for one pig): ")

last_digit = int(user_digits) % 10

second_digit = int(user_digits) // 10 % 10

first_digit = int(user_digits) // 100

sum_of_breaks = last_digit + second_digit + first_digit

breaks_for_pig = sum_of_breaks // 3

remaining = sum_of_breaks - (3 * breaks_for_pig)

print(sum_of_breaks)
print(breaks_for_pig)
print(remaining)
print(bool(remaining))
