def binarySearch(arr,l,r,x):
  if r>=1:
    mid = int(l + (r - 1)/2)
    if arr[mid] == x:
      return mid
    elif arr[mid] > x:
      return binarySearch(arr,l,mid-1,x)
    else:
      return binarySearch(arr,mid+1,r,x)
  else:
    return -1

arr = [2,3,4,10,40]
x = 10

result = binarySearch(arr,0,len(arr) - 1,x)

if result != -1:
  print("元素的索引为{}".format(result))
else:
  print("元素不在数组中")