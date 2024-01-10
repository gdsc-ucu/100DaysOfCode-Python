import datetime

current_date = datetime.date.today()

date_in_100days = current_date + datetime.timedelta(days=100)

print(f"Curent Date: {current_date}")
print(f"Date 100 Days from the Current Date: {date_in_100days}")
