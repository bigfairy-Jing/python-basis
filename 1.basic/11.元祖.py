# 元祖的元素不能修改 

tup1 = ('a','b','c','d')
tup2 = (1,2,3,4,5,6)
tup3 = 'd','e','f'

print(tup3)

tup4 = () # 空元祖

tup5 = tup1 + tup2
print(tup5)

lis = [1,2,3,4]
tup6 = tuple(lis)

print(lis,tup6)

# 所谓元组的不可变指的是元组所指向的内存中的内同不可变。

print(id(lis))