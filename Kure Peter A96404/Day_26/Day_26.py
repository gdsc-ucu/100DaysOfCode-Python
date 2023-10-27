import datetime
def daysAfter100():
    """
    Function to calculate the date after 100 days from now
    """
    today = datetime.date.today()
    date_after100 = today + datetime.timedelta(days = 100)
    return date_after100
print(daysAfter100().strftime("%A %B %d, %Y"))