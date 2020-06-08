year = int(input("输入一个年份"))

def getYearInfo(y):
  if(year%4) == 0:
    if(year%100)==0:
      if(year%400)==0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False


print(getYearInfo(year))
