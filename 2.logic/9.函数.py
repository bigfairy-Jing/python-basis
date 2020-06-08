# 函数 函数是组织好的，可重复使用的，用来实现单一，或相关联功能的代码段。
# 函数能提高应用的模块性，和代码的重复利用率。你已经知道Python提供了许多内建函数，比如print()。但你也可以自己创建函数，这被叫做用户自定义函数。

# 函数规则
  # 1.函数代码块以 def 关键词开头，后接函数标识符名称和圆括号()。
  # 2.任何传入参数和自变量必须放在圆括号中间，圆括号之间可以用于定义参数。
  # 3.函数的第一行语句可以选择性地使用文档字符串—用于存放函数说明。
  # 4.函数内容以冒号起始，并且缩进。
  # 5.return [表达式] 结束函数，选择性地返回一个值给调用方。不带表达式的return相当于返回 None。

def hello():
  print("hello Fairy")

hello()

def area(width,height):
  return width*height

print(area(10,10))


# 可更改(mutable)与不可更改(immutable)对象
def ChangeInt(a):
  a = 10

b = 2

ChangeInt(b)
print(b) # 2

def changeme(mylist):
  "修改传入的列表"
  mylist.append([1,2,3,4])
  return 

mylist = [10,20,30]
changeme(mylist)
print(mylist)


# 函数参数不需要指定顺序
def printinfo(name,age):
  "打印任何传入的字符串"
  print("名字",name)
  print("年龄",age)
  return

printinfo(age=50,name="runoob")

# 默认参数
#可写函数说明
def printinfo(name, age=35):
   "打印任何传入的字符串"
   print("名字: ", name)
   print("年龄: ", age)
   return


#调用printinfo函数
printinfo(age=50, name="runoob")
print("------------------------")
printinfo(name="runoob")

# 1.加了* 号的参数会以元祖的形式导入，存放 在所有未命名的变量参数
def printinfo(arg1,*vartuple):
  print(arg1)
  print(vartuple)

printinfo(70,60,50)

# 2.加了** 会以字典的形式导入 注意这里是字典，就要有key
def printinfo2(arg1,**vardict):
  print(arg1)
  print(vardict)

printinfo2(1,a=1,b=2)

# 3.声明函数 可以出现单独* ，但是*后的参数必须是用关键字传入
def f(a,*,b):
  return a + b

# f(1,2)# 报错
print(f(1,b=2))


# 匿名函数 
  # lambda 只是一个表达式，函数体比 def 简单很多。
  # lambda的主体是一个表达式，而不是一个代码块。仅仅能在lambda表达式中封装有限的逻辑进去。
  # lambda 函数拥有自己的命名空间，且不能访问自己参数列表之外或全局命名空间里的参数。
  # 虽然lambda函数看起来只能写一行，却不等同于C或C++的内联函数，后者的目的是调用小函数时不占用栈内存从而增加运行效率。

sum = lambda ar1,ar2:ar1+ar2
print(sum(1, 2))

# return 语句 不带参数的return语句 默认返回None

