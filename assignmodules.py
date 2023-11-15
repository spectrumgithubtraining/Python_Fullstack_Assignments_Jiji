# 1. Programs to implement the   of calendar module.
# Python program to display calendar of
# given month of the year

# import module

# import calendar

# Now you can use functions and classes from the calendar module
# Python program to display calendar of
# given month of the year


import calendar

yy = 2017
mm = 11

# # display the calendar
print(calendar.month(yy, mm))


# # Program to display calendar of the given month and year

# importing calendar module
import calendar

# yy = 2014  # year
# mm = 11    # month

# # To take month and year input from the user
yy = int(input("Enter year: "))
mm = int(input("Enter month: "))

# # display the calendar
print(calendar.month(yy, mm))

# #prgm to check leap yera or not

import calendar

def check_leap_year(year):
    if calendar.isleap(year):
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")

if __name__ == "__main__":
    year = int(input("Enter a year to check if it's a leap year: "))
    check_leap_year(year)


import calendar

yy = 2023
mm = 1
day = 15

weekday = calendar.weekday(yy, mm, day)

print(weekday)


# 2. Write Programs to implement datetime module ?
# Program to get the current date and time:
import datetime

now = datetime.datetime.now()

print(now)

# Program to add 10 days to the current date:
# import datetime

now = datetime.datetime.now()

ten_days_later = now + datetime.timedelta(days=10)

print(ten_days_later)

# Program to find the difference between two dates:
import datetime

start_date = datetime.datetime(2023, 1, 1)
end_date = datetime.datetime(2023, 12, 31)

difference = end_date - start_date

print(difference)
# Program to format a date and time:
import datetime

now = datetime.datetime.now()

formatted_date = now.strftime("%d-%m-%Y %H:%M:%S")

print(formatted_date)


#3. Write Programs to implement time module (includes formatting) ?

# Program to get the current time:
import time

now = time.time()

print(now)
