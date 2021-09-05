import calendar

input_date = input("Enter a date: ")

day = input_date[0:2]
month = input_date[3:5]
year = input_date[6:]
calendar.weekday(int(day), int(month), int(year))
