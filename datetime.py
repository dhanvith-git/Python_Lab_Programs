from datetime import date,datetime, timedelta
today = date.today()
now = datetime.now()
print(today)
print(now)
bd = date(2007, 7, 6)  
temp = now.strftime("%Y-%m-%d %H:%M:%S")
print(temp)
print(bd)