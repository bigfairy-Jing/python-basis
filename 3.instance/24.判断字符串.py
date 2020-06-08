# # 判断字符串是否存在子字符串
# str1 = input("请输入字符串1")
# str2 = input("请输入字符串2")

# def check(string,sub_str):
#   if(string.find(sub_str) == -1):
#     print("不存在！")
#   else:
#     print('存在')

# check(str1,str2)

# # 使用正则表达式提取字符串中的URL
# import re

# def Find(string):
#   url = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', string)
#   return url

# str3 = input("请输入要提取的字符串")
# print("urls",Find(str3))

# 将字符串作为代码执行
def exec_code():
  LOC = """
def factorial(num): 
  fact=1 
  for i in range(1,num+1): 
      fact = fact*i 
  return fact 
print(factorial(5))
"""
  exec(LOC)

exec_code()