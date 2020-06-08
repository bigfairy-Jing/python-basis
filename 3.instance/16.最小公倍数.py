def lcm(x,y):
  if(x>y): 
    getattr = x
  else:
    getattr = y
  
  while(True):
    if(getattr%x==0)and (getattr%y==0):
      lcm = getattr
      break
    getattr += 1
  
  return lcm


num1 = int(input("输入第一个数字: "))
num2 = int(input("输入第二个数字: "))

print('{0}和{1}的最小公倍数是{2}'.format(num1,num2,lcm(num1,num2)))
