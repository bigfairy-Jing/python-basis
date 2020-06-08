from datetime import date
import os
print(os.getcwd()) # 返回当前工作目录

# os.chdir("/Users/shuai/python_hub/python_basic1/2.logic") # 设置当前工作目录

# os.system('mkdir today') # 执行系统命令mkdir

# print(dir(os))
# print(help(os))

# 针对日常的文件和目录管理任务，:mod:shutil 模块提供了一个易于使用的高级接口:

import shutil
shutil.copyfile('copy1.txt','copy3.txt')
# shutil.move('/build/executables', 'installdir') # 移动

# 文件通配符
import glob
pys = glob.glob('*.py')
# print(pys)

# 命令行参数
import sys
print(sys.argv)
# 错误输出重定向和程序种植
# sys.stderr.write('Warning, log file not found starting a new one\n')

# 字符串正则匹配
import re
res =  re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')
print(res)


# 数学
# math模块为浮点运算提供了对底层C函数库的访问
import math
print(math.cos(math.pi / 4))
print(math.log(1024,2))

# random 提供生成随机数的工具
import random
print(random.choice(['apple','pear','banana']))

print(random.sample(range(100),10))

print(random.random())

print(random.randrange(6))

# 访问互联网 urllib.request
from urllib.request import urlopen
for line in urlopen("http://www.baidu.com"):
  line = line.decode('utf-8')
  if 'EST' in line or 'EDT' in line:
    print(line)


# 日期和时间
# from datetime import date
# now = date.today
# print(now)

# date(2003, 12, 2)
# print(now)

# brithday = date(1993,8,8)
# age = now - brithday
# print(age.days,age)

# 数据压缩
print("==========数据压缩======================")
import zlib
s = b'witch which has which witches wrist watch'
print(len(s))
t = zlib.compress(s)
print(len(t))

zlib.decompress(t)
print(zlib.crc32(s))

# 性能度量 有些用户对了解解决同一问题的不同方法之间的性能差异很感兴趣。Python 提供了一个度量工具，为这些问题提供了直接答案。
from timeit import Timer
print(Timer('t=a; a=b; b=t', 'a=1; b=2').timeit())
print(Timer('a,b = b,a', 'a=1; b=2').timeit())

# 测试模块  doctest  unitteset
