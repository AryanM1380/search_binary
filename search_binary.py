import os 
os.system("cls")

def search (array , target,low , high):
       mid = (low + high) // 2
       while low < high:
              if target == array[mid]:
                     return mid
              elif target < array[mid]:
                     return search(array , target, low, mid - 1)
              elif target > array[mid]:
                     return search(array , target , mid + 1 , high)
              else:
                     return "unknown"


Mylist = [1,3,5,7,10,12,8,9]
target = 3
Mylist.sort()

print(f'Target is found : {search(Mylist,target,0,len(Mylist)-1)}')