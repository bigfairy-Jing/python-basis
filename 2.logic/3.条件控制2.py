
guess = 7
number = -1

print("数字猜字游戏")

while guess != number:
  guess = int(input("请输入你猜的数字"))

  if guess == number:
    print("恭喜猜对")
  elif guess > number:
    print("小了")
  elif guess < number:
    print("大了")