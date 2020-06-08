# 异常处理
import sys

while True:
  try:
    x = int(input("请输入一个数字"))
    break
  except ValueError:
    print("您输入的不是一个数字，请再次尝试输入！")
  

try:
  f = open("./write.text")
  s = f.readline()
  i = int(s.strip())
except OSError as err:
  print("OS error: {0}".format(err))
except ValueError:
  print("无法将数据转换成整数")
except:
  print("Unexpected error:",sys.exc_info()[0])
  raise

# else 语句发生在try语句没有发生任何异常的地方
try:
  pass
except expression as identifier:
  pass
else:
  pass

# 无论是否有异常发生都将执行最后的代码
try:
  pass
except expression as identifier:
  pass
finally:
  pass

# python 使用raise抛出一个异常
x = 10
if x > 5:
  raise Exception('x 不能大于5'.format(x))

# 