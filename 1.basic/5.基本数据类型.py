'''
Python 中的变量不需要声明。每个变量在使用前都必须赋值，变量赋值以后该变量才会被创建。
在 Python 中，变量就是变量，它没有类型，我们所说的"类型"是变量所指的内存中对象的类型。
等号（=）用来给变量赋值。
等号（=）运算符左边是一个变量名,等号（=）运算符右边是存储在变量中的值。例如：
'''
counter = 100 # 整型变量
miles = 1000.0 # 浮点型变量
name = "runoob" # 字符串

# 多个变量赋值
a=b=c=d=1
a,b,c,d = 1,2,3,'fairy'

# 标准数据类型

  # Number（数字）
  # String（字符串）
  # List（列表）
  # Tuple（元组）
  # Set（集合）
  # Dictionary（字典）

# 不可变数据 Number（数字）、String（字符串）、Tuple（元组）；
# 可变数据  List（列表）、Dictionary（字典）、Set（集合）。

# Number
'''
Python3 支持 int、float、bool、complex（复数）。
在Python 3里，只有一种整数类型 int，表示为长整型，没有 python2 中的 Long。
像大多数语言一样，数值类型的赋值和计算都是很直观的。
内置的 type() 函数可以用来查询变量所指的对象类型。
'''
e,f,g,h = 2,2.2,True,5+6j
print(type(e), type(f), type(g), type(h))

# isinstance 判断
a = 1111
print(isinstance(a,int))

# 注意：在 Python2 中是没有布尔型的，它用数字 0 表示 False，用 1 表示 True。到 Python3 中，把 True 和 False 定义成关键字了，但它们的值还是 1 和 0，它们可以和数字相加。

var1 = 1
var2 = 10 
print(var1,type(var1))

del var1
# print(var1)

# 加减乘除 取余 乘方 除法得到整数  / 返回一个浮点数  // 返回一个整数 
# 在混合计算 python 会把整型转换成浮点数类型
print(5 + 4)
print(4.3-1)
print(3*7)
print(2/4)
print(2//4)
print(17%3)
print(2**5)


# String  截取语法：变量[头下标:尾下标]

str = "Runoob"

print(str)  # log
print(str[0:-1])  # 0 到倒数第二个
print(str[0])  # 第一个
print(str[2:5])  # 第三个到第五个
print(str[2:])  # 第三个到结尾
print(str*2)  # 两次连接
print(str + '你好')  # 连接你好
print('hello\nrunoob')  # /n换行
print(r'hello\nrunoob')  # r /n 不换行

# Python中的字符串有两种索引方式，从左往右以0开始，从右往左以-1开始。 

# List 截取语法：变量[头下标:尾下标]   或者 变量[头下标:尾下标:步长] 这里的步长是间隔
'''
列表可以完成大多数集合类的数据结构实现。列表中元素的类型可以不相同，它支持数字，字符串甚至可以包含列表（所谓嵌套）。
列表是写在方括号 [] 之间、用逗号分隔开的元素列表。
和字符串一样，列表同样可以被索引和截取，列表被截取后返回一个包含所需元素的新列表。
'''

list = ['abcd',7,2.2,'runoob',70.0]

tinyList = [1,2,'runoob']
print("---------list-----------")
print(list)
print(list[0])
print(list[1:3])
print(list[2:])
print(tinyList*2)
print(list+tinyList)

# 与字符串不同列表中元素可变
a = [1,2,3,4,5,6]
a[0] = 9
a[1:3] = [6,'b']
print(a)
a[3:5] = []
print(a)

# 步长读取

b = [3,6,9,12,15]
print(b[1:5:2])


# 如果第三个参数为负数表示逆向读取，以下实例用于翻转字符串：
def reverseWords(input):
  inputWords = input.split(" ")
  inputWords=inputWords[-1::-1]
  output = " ".join(inputWords)
  return output

if __name__ == "__main__":
  input = 'I like runoob'
  rw = reverseWords(input)
  print(rw)


# Tuple 元祖
'''
元组（tuple）与列表类似，不同之处在于元组的元素不能修改。元组写在小括号 () 里，元素之间用逗号隔开。
元组中的元素类型也可以不相同：
'''

tuple = ('abcd', 786, 2.23, 'runoob', 70.2)
tinytuple = (123, 'runoob')

print(tuple)             # 输出完整元组
print(tuple[0])          # 输出元组的第一个元素
print(tuple[1:3])        # 输出从第二个元素开始到第三个元素
print(tuple[2:])         # 输出从第三个元素开始的所有元素
print(tinytuple * 2)     # 输出两次元组
print(tuple + tinytuple)  # 连接元组


tup1 = () # 空元祖
tup2 = (2,) # 一个元素 需要在元素后添加,

# Set 集合  不重复的集合

'''
集合（set）是由一个或数个形态各异的大小整体组成的，构成集合的事物或对象称作元素或是成员。
基本功能是进行成员关系测试和删除重复元素。
可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。
创建格式：
'''

pra1 = {1,2,3,5}
pra2 = set({1,3,4})

print(pra1)
print(pra2)

student = {'Tom','Jim',"Tom","Jim"}
print(student)

if "Rose" in student:
  print("Rose 在集合中")
else:
  print("Rose 不在集合中")

a = set('abracadabra')
b = set('alacazam')
print(a,b)

print(a - b)
print(a | b)
print(a&b)
print(a^b)

# Dictionary 字典

'''
字典（dictionary）是Python中另一个非常有用的内置数据类型。
列表是有序的对象集合，字典是无序的对象集合。两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。
字典是一种映射类型，字典用 { } 标识，它是一个无序的 键(key) : 值(value) 的集合。
键(key)必须使用不可变类型。
在同一个字典中，键(key)必须是唯一的。
'''
print("------------dict-------------------")
dict1 = {'name':'runoob','code':1,'site':'www'}
dict1['one'] = 'fairy'
print(dict1)
print(dict1.keys())
print(dict1.values())

dic2 =  dict([('Runoob', 1), ('Google', 2), ('Taobao', 3)])
print(dic2)


dic3 = {x: x**2 for x in (2,3,4)}
print(dic3)  # {2: 4, 3: 9, 4: 16}

dic4 = dict(a=1,b=2,c=3)
print(dic4)
# 注意
  # 1、字典是一种映射类型，它的元素是键值对。
  # 2、字典的关键字必须为不可变类型，且不能重复。
  # 3、创建空字典使用 {}。


# 数据类型转换

# int(x[, base])
# 将x转换为一个整数

# float(x)
# 将x转换到一个浮点数

# complex(real[, imag])
# 创建一个复数

# str(x)
# 将对象 x 转换为字符串

# repr(x)
# 将对象 x 转换为表达式字符串

# eval(str)
# 用来计算在字符串中的有效Python表达式, 并返回一个对象

# tuple(s)
# 将序列 s 转换为一个元组

# list(s)
# 将序列 s 转换为一个列表

# set(s)
# 转换为可变集合

# dict(d)
# 创建一个字典。d 必须是一个(key, value)元组序列。

# frozenset(s)
# 转换为不可变集合

# chr(x)
# 将一个整数转换为一个字符

# ord(x)
# 将一个字符转换为它的整数值

# hex(x)
# 将一个整数转换为一个十六进制字符串

# oct(x)
# 将一个整数转换为一个八进制字符串

