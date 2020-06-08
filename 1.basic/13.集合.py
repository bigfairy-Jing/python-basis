# 集合（set）是一个无序的不重复元素序列。

set1 = set() # 创建一个空集  必须使用set() 而不是 { } 因为 {} 表示一个空字典

# 这里的集合跟数学中的集合相似

# 添加元素

set2 = set(("do","re","mi"))
set2.add("fa")
print(set2)

set2.update([5,6],[7])
print(set2)  # {'mi', 5, 6, 7, 'fa', 're', 'do'}

# 注意这里的set 容器是无序的

# 移除元素
set2.remove(5)
print(set2)

# set2.remove(9) # 不存在会发生错误

set2.discard(10) # 也是移除元素但是不存在不会发生错误

set2.pop() # 随机删除集合中一个元素，注意这里是随机，因为集合无序

print(len(set2))

set2.clear()

print("f" in set2)

'''
add()	为集合添加元素
clear()	移除集合中的所有元素
copy()	拷贝一个集合
difference()	返回多个集合的差集
difference_update()	移除集合中的元素，该元素在指定的集合也存在。
discard()	删除集合中指定的元素
intersection()	返回集合的交集
intersection_update()	返回集合的交集。
isdisjoint()	判断两个集合是否包含相同的元素，如果没有返回 True，否则返回 False。
issubset()	判断指定集合是否为该方法参数集合的子集。
issuperset()	判断该方法的参数集合是否为指定集合的子集
pop()	随机移除元素
remove()	移除指定元素
symmetric_difference()	返回两个集合中不重复的元素集合。
symmetric_difference_update()	移除当前集合中在另外一个指定集合相同的元素，并将另外一个指定集合中不同的元素插入到当前集合中。
union()	返回两个集合的并集
update()	给集合添加元素
'''
