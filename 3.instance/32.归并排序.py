'''
归并排序（英语：Merge sort，或mergesort），是创建在归并操作上的一种有效的排序算法。该算法是采用分治法（Divide and Conquer）的一个非常典型的应用。

分治法:

分割：递归地把当前序列平均分割成两半。
集成：在保持元素顺序的同时将上一步得到的子序列集成到一起（归并）。
'''

##  这里待优化

def merge(arr,l,m,r):
  n1 = m - l + 1
  n2 = r - m 

  L = [0]*(n1)
  R = [0]*(n2)

  for i in range(0,n1):
    L[i] = arr[l+i]

  for j in range(0,n2):
    R[j] = arr[m + 1 + j]
  
  i = 0
  j = 0
  k  = 0

  while i<n1 and j < n2:
    if L[i] <= R[j]:
      arr[k] = L[i]
      i+=1
    else:
      arr[k] = R[j]
      j+=1
    k+=1
  
  while i<n1:
    arr[k] = L[i]
    i+=1
    k+=1

  while j<n2:
    arr[k] = R[j]
    j+=1
    k+=1

def mergeSort(arr,l,r): # 0 6    03    36
  if l<r:   
    m = int((l+(r-1))/2)

    mergeSort(arr, l, m)
    mergeSort(arr, m+1, r)
    merge(arr, l, m, r)
  

arr = [12, 11, 13, 5, 6, 7]
n = len(arr)

print(arr)
mergeSort(arr,0,n-1)
print(arr)


    
