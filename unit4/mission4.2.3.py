input_temp = input("Insert the temperature you would like to convert: ")

temp = input_temp[0:len(input_temp) - 1]
sign = input_temp[len(input_temp) - 1]

if sign == ('F' or 'f'):
    new_temp = (5 * float(temp) - 160) // 9
    print(str(new_temp) + 'C')
else:
    new_temp = (9 * float(temp) + (32 * 5)) // 5
    print(str(new_temp) + 'F')


