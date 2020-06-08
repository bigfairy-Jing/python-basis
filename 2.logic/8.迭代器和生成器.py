# 迭代器有两个基本的方法：iter() 和 next()。

# 字符串，列表或元组对象都可用于创建迭代器：

lis = [1,2,3,4]
it = iter(lis)   # 生成一个迭代器对象
print(next(it))
print(next(it))

# for语句可以迭代迭代器
# for x in it:
#   pass
#   print(x,end=" ") # 这里只打印3，4 因为前面已经迭代了1，2
# import sys

# list = [1,2,3,4]
# it = iter(list)
# while True:
#   try:
#     print(next(it))
#   except StopIteration:
#     sys.exit()
#     pass


# 创建一个返回数字的迭代器，初始值为1，逐步递增1

# 把一个类作为一个迭代器使用需要在类中实现两个方法 __iter__() 与 __next__() 。
# Python 的构造函数为 __init__(), 它会在对象初始化的时候执行。 （js的构造函数是constructor）

# __iter__() 方法返回一个特殊的迭代器对象， 这个迭代器对象实现了 __next__() 方法并通过 StopIteration 异常标识迭代的完成。
# __next__() 方法（Python 2 里是 next()）会返回下一个迭代器对象。

class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self
  def __next__(self):
    if self.a <= 20:
      x=self.a
      self.a += 1
      return x
    else:
      raise StopIteration

myClass = MyNumbers()
myiter = iter(myClass)

print("--------R-------")
for x in myiter:
  print(x)


# 生成器
# 在 Python 中，使用了 yield 的函数被称为生成器（generator）。

# 跟普通函数不同的是，生成器是一个返回迭代器的函数，只能用于迭代操作，更简单点理解生成器就是一个迭代器。

# 生成器是一个返回迭代器的函数 ，这里返回一个斐波那契数列
import sys

def fibonacci(n):
  a,b,counter = 0 , 1, 0
  while True:
    if(counter>n):
      return 
    yield a
    a,b = b ,a + b
    counter += 1
  
f = fibonacci(10)

while True:
  try:
    print(next(f),end=" ")
    pass
  except StopIteration:
    sys.exit()