import time

print("按下回车开始倒计时，按下Ctrl + c停止计时")

while True:
  input("")
  starttime = time.time()
  print("开始")
  try:
    while True:
      print("计时:",round(time.time() - starttime,0),'秒')
      time.sleep(1)
  except KeyboardInterrupt:
    print('结束')
    endtime = time.time()
    print('总共的时间为：',round(endtime - starttime,2),'secs')
    break