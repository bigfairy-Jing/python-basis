# python中数字有四种类型：整数、布尔型、浮点数和复数。
  # int(整数), 如 1, 只有一种整数类型 int，表示为长整型，没有 python2 中的 Long。
  # bool(布尔), 如 True。
  # float(浮点数), 如 1.23、3E-2
  # complex(复数), 如 1 + 2j、 1.1 + 2.2j

#!/usr/bin/python3

# 字符串
  # python中单引号和双引号使用完全相同。
  # 使用三引号('''或""")可以指定一个多行字符串。
  # 转义符 '\'
  # 反斜杠可以用来转义，使用r可以让反斜杠不发生转义。。 如 r"this is a line with \n" 则\n会显示，并不是换行。
  # 按字面意义级联字符串，如"this " "is " "string"会被自动转换为this is string。
  # 字符串可以用 + 运算符连接在一起，用 * 运算符重复。
  # Python 中的字符串有两种索引方式，从左往右以 0 开始，从右往左以 -1 开始。
  # Python中的字符串不能改变。
  # Python 没有单独的字符类型，一个字符就是长度为 1 的字符串。
  # 字符串的截取的语法格式如下：变量[头下标:尾下标:步长]

word = "字符串"
sentence = "这是一个句子"
paragraph = """这是一个段落，
可以由多个行组成
"""

print(word)


str = "Runoob"

print(str) #log
print(str[0:-1]) # 0 到倒数第二个
print(str[0]) # 第一个
print(str[2:5]) # 第三个到第五个
print(str[2:])  # 第三个到结尾
print(str*2)  # 两次连接 
print(str + '你好')  # 连接你好
print('hello\nrunoob') # /n换行
print(r'hello\nrunoob') # r /n 不换行


# Python可以在同一行中使用多条语句，语句之间使用分号(;)分割，以下是一个简单的实例：

import sys; x = 'runoob'; sys.stdout.write(x + '\n')


# 

















