class myClass:
  """一个简单的类实例"""
  i = 12345
  def f(self):
    return 'hello world'


x = myClass()

print(x.i,x.f())

# __init__ 会在类实例化时候自动调用

class Complex:
  def __init__(self,realpart,imagpart):
    print("自动打印了这些内容")
    self.r = realpart
    self.a = imagpart
  

x = Complex(3.0, -4.5)
print(x.r,x.a)

# self 代表类的实例，而非类
# 类的方法与普通的函数只有一个特别的区别——它们必须有一个额外的第一个参数名称, 按照惯例它的名称是 self。

class Test:
  def prt(self):
    print(self)
    print(self.__class__)
    print(self.__class__ == Test)
  
t = Test()
t.prt()


# 类的方法 在类的内部，使用 def 关键字来定义一个方法，与一般函数定义不同，类方法必须包含参数 self, 且为第一个参数，self 代表的是类的实例
print("-----------类的方法------------")

class people:
  name = ""
  age = 0
  __weight = 0
  def __init__(self,n,a,w):
    self.name = n
    self.age = a
    self.__weight = w
  def speak(self):
    print("%s 说：我 %d 岁"%(self.name,self.age))

p = people('帅',10,30)
p.speak()

# 继承

class student(people):
  grade = ''
  def __init__(self,n,a,w,g):
    people.__init__(self,n,a,w)
    self.grade = g
  def speak(self):
    print("%s 说: 我 %d 岁了，我在读 %d 年级" % (self.name, self.age, self.grade))

s = student('帅',10,60,3)
s.speak()

# 多继承
# 需要注意圆括号中父类的顺序，若是父类中有相同的方法名，而在子类使用时未指定，python从左至右搜索 即方法在子类中未找到时，从左到右查找父类中是否包含方法。

class speaker():
  topic = ''
  name = ''
  def __init__(self,n,t):
    self.name = n
    self.topic = t
  def speak(self):
    print("我叫 %s，我是一个演说家，我演讲的主题是 %s" % (self.name, self.topic))

class sample(speaker,student):
  a = ''
  def __init__(self,n,a,w,g,t):
    student.__init__(self,n,a,w,g)
    speaker.__init__(self,n,t)
  
test = sample("Tim",25,80,4,"python")
test.speak()


print("-----------方法重写----------------")
# 方法重写
class Parent:
  def myMethod(self):
    print("调用父类方法")

class Child(Parent):
  def myMethod(self):
    print("调用子类方法")

c = Child()
c.myMethod()
super(Child,c).myMethod() # 用子类对象调用父类已经被覆盖的方法

print("---------------类的属性与方法---------")
# __private_attrs：两个下划线开头，声明该属性为私有，不能在类的外部被使用或直接访问。在类内部的方法中使用时 self.__private_attrs。
# __private_method：两个下划线开头，声明该方法为私有方法，只能在类的内部调用 ，不能在类的外部调用。self.__private_methods。

class JustCounter:
  __secretCount = 0
  publicCount = 0
  def count(self):
    self.__secretCount +=1
    self.publicCount += 1
    print(self.__secretCount)

counter = JustCounter()
counter.count()
counter.count()

print(counter.publicCount)
# print(counter.__secretCount)

class Site:
  def __init__(self,name,url):
    self.name = name
    self.__url = url
  def who(self):
    print('name :',self.name)
    print('url:',self.__url)
  def __foo(self):
    print("这是私有方法")
  def foo(self):
    print("这是共有方法")
    self.__foo

x = Site("周杰伦",'http://www.baidu.com')
x.who()
x.foo()
# x.__foo()


'''
类的专有方法
__init__ : 构造函数，在生成对象时调用
__del__ : 析构函数，释放对象时使用
__repr__ : 打印，转换
__setitem__ : 按照索引赋值
__getitem__: 按照索引获取值
__len__: 获得长度
__cmp__: 比较运算
__call__: 函数调用
__add__: 加运算
__sub__: 减运算
__mul__: 乘运算
__truediv__: 除运算
__mod__: 求余运算
__pow__: 乘方
'''

# 运算符重载
class Vector:
  def __init__(self,a,b):
    self.a = a
    self.b = b
  def __str__(self):
    return 'Vector (%d,%d)'%(self.a,self.b)
  def __add__(self,other):
    return Vector(self.a + other.a,self.b + other.b)


v1 = Vector(2,10)
v2 = Vector(5,-2)
print(v1 + v2)


















