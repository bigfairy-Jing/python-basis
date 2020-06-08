# break 语句可以跳出 for 和 while 的循环体。如果你从 for 或 while 循环中终止，任何对应的循环 else 块将不执行。
# continue 语句被用来告诉 Python 跳过当前循环块中的剩余语句，然后继续进行下一轮循环。


# 循环语句可以有 else 子句，它在穷尽列表(以for循环)或条件变为 false(以while循环)导致循环终止时被执行，但循环被 break 终止时不执行。
# 如下实例用于查询质数的循环例子:

# 查询10000 到 20000 之间的质数的个数

lis = []

for n in range(10000,20000):
  for x in range(2,n):
    if(n%x == 0):
      # print(n, '等于', x, '*', n//x)
      break
  else:
    lis.append(n)
    print(n,"是质数")

print("10000-20000之间的质数的个数是",len(lis))


# pass 语句
# Python pass是空语句，是为了保持程序结构的完整性。
