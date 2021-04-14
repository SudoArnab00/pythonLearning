from datetime import date
from datetime import time
from datetime import datetime
today = date.today()
print("Today's date: ",today)
print("Date components: ",today.day, today.month, today.year)

days = ["mon","Tue","Wed","Thu","Fri"]
print(days[today.weekday()])