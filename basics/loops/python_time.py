import time
import calendar

print("Time from 1970 till now", time.time())


print("Formatted Time", time.asctime(time.localtime(time.time())))


# Python Sleep
print("Python Sleep Activates Now!")
for i in range(0, 5):
    print(i, "th second")
    # Each element will be printed after 1 second
    time.sleep(1)

cal = calendar.month(2021, 12)
# printing the calendar of December 2020
print(cal)

print("Calender for the year -")
# printing the calendar of the year 2019
s = calendar.prcal(2021)
