# 三种命名空间
  # 1.内置名称（built-in names）， Python 语言内置的名称，比如函数名 abs、char 和异常名称 BaseException、Exception 等等。
  # 2.全局名称（global names），模块中定义的名称，记录了模块的变量，包括函数、类、其它导入的模块、模块级的变量和常量。
  # 3.局部名称（local names），函数中定义的名称，记录了函数的变量，包括函数的参数和局部定义的变量。（类中定义的也是）

# 包含顺序 内置命名空间>>>>全局命名空间>>>>>局部命名空间
# 查找顺序 局部命名空间>>>>内置命名空间>>>>>内置命名空间

# 作用域

# L（Local）：最内层，包含局部变量，比如一个函数/方法内部。
# E（Enclosing）：包含了非局部(non-local)也非全局(non-global)的变量。比如两个嵌套函数，一个函数（或类） A 里面又包含了一个函数 B ，那么对于 B 中的名称来说 A 中的作用域就为 nonlocal。
# G（Global）：当前脚本的最外层，比如当前模块的全局变量。
# B（Built-in）： 包含了内建的变量/关键字等。，最后被搜索

g_count = 0  # 全局作用域
def outer():
    o_count = 1  # 闭包函数外的函数中

    def inner():
        i_count = 2  # 局部作用域


# Python 中只有模块（module），类（class）以及函数（def、lambda）才会引入新的作用域，其它的代码块（如 if/elif/else /、try/except、for/while等）是不会引入新的作用域的，也就是说这些语句内定义的变量，外部也可以访问，如下代码：

if True:
  msg = 'I am from Run'

print(msg)

# 当内部想要修改外部作用域的变量是，就要用到global和nonlocal关键字了
print("---------------------global-----------------------")
num = 1
def fun1():
  global num
  print(num)
  num = 123
  print(num)

fun1()
print(num)
# 如果需要修改嵌套作用域关键字变量就要用nonlocal关键字了
def outer():
  num = 10
  def inner():
    nonlocal num
    num = 100
    print(num)
  inner()
  print(num)
outer()