def hcf(x,y):
  """返回两个数的最大公约数"""
  if x>y:
    smaller = y
  else:
    smaller = x
  for i in range(1,smaller + 1):
    if((x%i == 0) and (y%i==0 )):
      s = i
  return s

num1 = int(input("请输入第一个数"))
num2 = int(input("请输入第二个数"))

print('{0}和{1}的最大公约数是{2}'.format(num1,num2,hcf(num1,num2)))