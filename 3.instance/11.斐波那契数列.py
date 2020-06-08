ns = int(input("你需要几项？"))

n1 = 0
n2 = 1
count = 2

if ns <= 0:
  print("请输入一个正整数。")
elif ns == 1:
  print(n1)
else:
  print("斐波那契数列：")
  print(n1, ",", n2, end=" , ")
  while count < ns:
    nth = n1 + n2
    print(nth,end=" ,")
    n1 = n2 
    n2 = nth
    count += 1
