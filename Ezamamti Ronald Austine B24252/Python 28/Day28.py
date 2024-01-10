import math
from datetime import datetime

current_date = datetime.now()

day_of_month = current_date.day

square_root_of_the_day = math.sqrt(day_of_month)

print("Current date:", current_date.strftime("%Y-%m-%d"))

print(f"The square root of the day of the month is {square_root_of_the_day:.2f}")