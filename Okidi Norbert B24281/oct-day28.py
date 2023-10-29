import math
import datetime

current_date = datetime.date.today()

day_of_month = current_date.day

squart_root = math.sqrt(day_of_month)

print(f"The square root of the day {day_of_month} of the month is {squart_root}")
