#!/usr/bin/python3
# for x in range(1,11):
#   print('{0:2d}{1:3d}{2:4d}'.format(x,x**x,x*x*x))

# f = open("./out.py","w")
# f.write("python write test>python write testpython write testpython write testpython write testpython write testpython write testpython write testpython write testpython write testpython write testpython write testpython write testpython write testpython write testpython write testpython write testpython write testpython write testpython write testpython write testpython write testpython write testpython write test")
# f.close()

f = open("./out.py","r")
print(f.read())

f = open("./out.py","w")
num = f.write("python \n是一个非常好的语言，\n的确非常的好")
print(num)
f.close()

print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

f = open("./write.text","w")
value = ('www.baidu.com',14)
s = str(value)
f.write(s)


print(f.tell())

f.close()

with open("./write.text") as target:
  print(target.read())
  pass

print(f.closed)

print("=========pickle==========")

import pickle

data1 = {
  "a":[1,2.0,4+6j],
  "b":("string",u"Unicode string"),
  "c":None
}

selfref_list = [1,2,3]
selfref_list.append(selfref_list)

output = open('data.pkl', 'wb')

pickle.dump(data1,output)

pickle.dump(selfref_list,output,-1)

output.close()








