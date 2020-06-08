
def factorial(num):
  f = 1
  if num<0:
    print("抱歉,负数没有阶乘")
  elif num == 0:
    print("0的阶乘是1")
    pass
  else:
    for i in range(1,num + 1):
      f = f*i
    print("{0}的阶乘是{1}".format(num,f))
  

number = int(input("请输入请求阶乘的数字"))
factorial(number)