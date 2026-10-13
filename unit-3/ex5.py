import datetime


x=datetime.datetime.now()
print("Current Date and Time:",x)

print("Year:",x.year)
print("Month:",x.month)
print("Day:",x.day)
print("Hour:",x.hour)
print("Minute:",x.minute)
print("Second:",x.second)

today=datetime.date.today()
print("today:",today)


future=today+datetime.timedelta(days=5)
past=today-datetime.timedelta(days=5)

print("future date:",future)
print("past date:",past)


print("----Date Difference----")
date1=datetime.date(2024,6,10)
date2=datetime.date(2024,6,20)
diff=date2-date1
print("Difference in days:",diff.days)

# strftime

print("----strftime-------")
print(x.strftime("%d-%m-%Y"))
print(x.strftime("%d %B %Y"))
print(x.strftime("%A"))
print(x.strftime("%b"))
print(x.strftime("%B"))
print(x.strftime("%c"))
print(x.strftime("%x"))
print(x.strftime("%X"))
print(x.strftime("%I:%M:%S %p"))



