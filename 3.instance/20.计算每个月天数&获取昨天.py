import calendar

yy = int(input("输入年份"))
mm = int(input("输入月份"))

mothRange = calendar.monthrange(yy,mm)
print('所查月份第一天是周{0}, 共有{1}天'.format(list(mothRange)[0], list(mothRange)[1]))


# 获取昨天日期
import datetime

def getYes():
  today = datetime.date.today()
  oneday = datetime.timedelta(days=1)
  yesterday = today - oneday
  return yesterday

print(getYes())