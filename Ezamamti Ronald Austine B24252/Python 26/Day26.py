from datetime import datetime, timedelta

current_date = datetime.now()
future_date = current_date + timedelta(days=100)
print("Current date:", current_date.strftime("%Y-%m-%d"))
print("Date 100 Days from the current date:", future_date.strftime("%Y-%m-%d"))