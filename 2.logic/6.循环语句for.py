languages = ["javascript","python","c","c++"]
for language in languages:
  print(language)


# 跳出循环
for la in languages:
  if la == 'c':
    print("c,跳出循环")
    break
  print("循环数据",la)
else:
  print("没有循环数据")

print("完成循环")


# range函数
for i in range(10):
  print(i)

for i in range(5,9):
  print(i)


for i in range(1,10,2): # 第三个参数步长
  print(i)

# range 创建列表
lis = list(range(10))


# break 语句可以跳出 for 和 while 的循环体。如果你从 for 或 while 循环中终止，任何对应的循环 else 块将不执行。

# continue 语句被用来告诉 Python 跳过当前循环块中的剩余语句，然后继续进行下一轮循环。

