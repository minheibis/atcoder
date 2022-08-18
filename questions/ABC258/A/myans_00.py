from datetime import datetime, timedelta

K = int(input())

dt1 = datetime(year=2017, month=10, day=10, hour=21)
dt2 = dt1 + timedelta(minutes=K)

print(dt2.strftime("%H:%M"))
