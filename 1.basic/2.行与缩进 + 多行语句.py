
if True:
  print("True")
else:
  print("False")


if True:
  print("True")
else:
    # print("False") # 缩进不一致，会导致运行错误
  print("False")  


# Python 通常是一行写完一条语句，但如果语句很长，我们可以使用反斜杠(\)来实现多行语句，例如：

# total = item_one + \
#         item_two + \
#         item_three

total = ['item_one', 'item_two', 'item_three',
        'item_four', 'item_five']

print(total)

# 多个语句构成代码组

'''
缩进相同的一组语句构成一个代码块，我们称之代码组。
像if、while、def和class这样的复合语句，首行以关键字开始，以冒号( : )结束，该行之后的一行或多行代码构成代码组。
我们将首行及后面的代码组称为一个子句(clause)。
'''
'''
例如：
if expression : 
   suite
elif expression : 
   suite 
else : 
   suite
'''

# Print默认输出是换行的，如果要实现不换行需要在变量末尾加上 end=""

# 不换行输出
print(123456,end=" ")
print(654321,end=" ")
print()
