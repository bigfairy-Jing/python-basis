import time

a1 = "2019-5-10 23:59:00"

timeArray = time.strptime(a1, "%Y-%m-%d %H:%M:%S")
print(timeArray)

timeStamp = int(time.mktime(timeArray))

print(timeStamp)

a2 = "2019/5/10 23:59:00"
timeArray = time.strptime(a2, "%Y/%m/%d %H:%M:%S")
otherStyleTime = time.strftime("%Y/%m/%d %H:%M:%S", timeArray)
print(otherStyleTime)
