import sys
import out

for i in sys.argv:
  print(i)

print('\n\nPython 路径为：', sys.path, '\n')

out.printInfo(1)



#

def fib(n):
  a,b = 0 ,1
  while b<n:
    print(b,end="")
    a,b = b,a+b
  print()

# 

def fib2(n):
  result = []
  a,b = 0 , 1
  while b < n:
    result.append(b)
    a,b = b , a + b
  return result

print(__name__)

print(dir(out),dir(sys))

print("-----------------print-----------")

print(dir())

# 深入模块

