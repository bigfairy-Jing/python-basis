### 数字求和

print('两个数字之和是 %.1f'%(float(input('请输入第一个数字')) + float(input("请输入第二个数字"))))

### 平方跟 # 这里正数可以用 num**0.5
import cmath
num = int(input("请输入一个数字: "))
if num>=0:
  print('{0}的平方根为{1}'.format(num,num**0.5))
else:
  num_sqrt = cmath.sqrt(num)
  print('{0} 的平方根为{1:0.3f}+{2:0.3f}j'.format(num,num_sqrt.real,num_sqrt.imag))