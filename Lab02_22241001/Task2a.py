#2(1)

def merge(left_arr, right_arr):
  new_arr = []
  i = 0
  j = 0
  while i < len(left_arr) and j < len(right_arr):
    if int(left_arr[i]) < int(right_arr[j]):
      new_arr += [left_arr[i]]
      i += 1
    else:
      new_arr += [right_arr[j]]
      j += 1
  if i < len(left_arr):
    new_arr += left_arr[i:]
  if j < len(right_arr):
    new_arr += right_arr[j:]
  return new_arr


def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr)//2
        left_arr = mergeSort(arr[:mid])
        right_arr = mergeSort(arr[mid:])
        return merge(left_arr, right_arr)


file = open("input2.txt", "r")
output = open("output2a.txt", "w")
n = m = 0
listN, listM = [], []
for i2 in range(4):
  file.readline()
  listN = file.readline().rstrip().split(" ")
  m = int(file.readline())
  listM = file.readline().rstrip().split(" ")
  for j1 in mergeSort(listN + listM):
    output.write(j1 + " ")
  output.write("\n")
file.close()
output.close()

#nlogn merge sort er time complexity

