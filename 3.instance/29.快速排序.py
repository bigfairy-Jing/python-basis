'''
快速排序使用分治法（Divide and conquer）策略来把一个序列（list）分为较小和较大的2个子序列，然后递归地排序两个子序列。

步骤为：

挑选基准值：从数列中挑出一个元素，称为"基准"（pivot）;
分割：重新排序数列，所有比基准值小的元素摆放在基准前面，所有比基准值大的元素摆在基准后面（与基准值相等的数可以到任何一边）。在这个分割结束之后，对基准值的排序就已经完成;
递归排序子序列：递归地将小于基准值元素的子序列和大于基准值元素的子序列排序。
递归到最底部的判断条件是数列的大小是零或一，此时该数列显然已经有序。

选取基准值有数种具体方法，此选取方法对排序的时间性能有决定性影响。
'''

def partition(arr,low,high):
  i = (low - 1) # -1
  pivot = arr[high] # last

  for j in range(low,high): # -1 4   -1 0 1 2 3
    if arr[j] <= pivot: # 0 1  2 3 4 
      i = i + 1 # i = 0
      arr[i],arr[j] = arr[j],arr[i] #

  arr[i + 1],arr[high] = arr[high],arr[i+1]
  return (i+1)


def quickSort(arr,low,high):
  if low < high:
    pi = partition(arr,low,high)
    quickSort(arr,low,pi-1)
    quickSort(arr,pi+1,high)


arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSort(arr, 0, n-1)
print(arr)
