#!/usr/bin/python3
# Filename: support.py

from collections import deque

queue = deque(["John","Eric","Fairy"])
print(queue)
queue.append("Terry")
print(queue)
queue.append("Zhou")
print(queue)
queue.popleft()
print(queue)

# 列表推导式 (改变 以及过滤都可以)
print([3*x for x in [2,3,4,5]])
print([[3*x,x**x] for x in [2,3,4,5]])

freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']

print([peo.strip() for peo in freshfruit])

print([x*x for x in [1,2,3] if x >= 2])

# 技巧
vec1 = [2, 4, 6]
vec2 = [4, 3, -9]
[x*y for x in vec1 for y in vec2]
#[8, 6, -18, 16, 12, -36, 24, 18, -54]
[x+y for x in vec1 for y in vec2]
#[6, 5, -7, 8, 7, -5, 10, 9, -3]
[vec1[i]*vec2[i] for i in range(len(vec1))]
#[8, 12, -54]

# 嵌套列表解析
matrix = [
  [1,2,3,4],
  [5,6,7,8],
  [9,10,11,12,13]
]

print([[row[i] for row in matrix] for i in range(4)])

# del 语句

# 元祖 和 序列
t = 123,2,"hello"
print(t)

u = t,(1,2,3,4)
print(u)

# 集合

# 字典

knights = {'gallahad': 'the pure', 'robin': 'the brave'}

for k,v in knights.items():
  print(k,v)

for i,v in enumerate(["tic","tac","toe"]):
  print(i,v)

# 同时遍历多个
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']

for q,a in zip(questions,answers):
  print('{0} and {1}'.format(q,a))

# 要按顺序遍历一个序列，使用 sorted() 函数返回一个已排序的序列，并不修改原值
basket = ['apple','orange','apple','pear','orage','banana']

for f in sorted(set(basket)):
  print(f)


def printInfo(x):
  print(x)
