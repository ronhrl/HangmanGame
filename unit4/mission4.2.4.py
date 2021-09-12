import calendar

input_date = input("Enter a date: ")

day = input_date[0:2]
month = input_date[3:5]
year = input_date[6:]

day_in_year = calendar.weekday(int(year), int(month), int(day))
print(day_in_year)

if day_in_year == -1:
    print("Sunday")

elif day_in_year == 0:
    print("Monday")

elif day_in_year == 1:
    print("Tuesday")

elif day_in_year == 2:
    print("Wednesday")

elif day_in_year == 3:
    print("Thursday")

elif day_in_year == 4:
    print("Friday")

elif day_in_year == 5:
    print("Saturday")
