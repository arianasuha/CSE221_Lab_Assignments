def quickSort(arr, start = 0, end = 0):
  if start >= end:
    return arr
  else:
    partition_ind = partition(arr, start, end)
    quickSort(arr, start, partition_ind - 1)
    quickSort(arr, partition_ind + 1, end )
    return arr


def partition(arr, start, end):
  pivot = arr[end]
  pindex = start
  for i in range(start,end):
    if arr[i] <= pivot:
      arr[i], arr[pindex] = arr[pindex], arr[i]
      pindex += 1
  arr[pindex], arr[end] = arr[end], arr[pindex]
  return pindex

with open("input5.txt", "r") as file:
  with open("output5.txt", "w") as file2:
    for line in file:
        line = next(file).strip().split()
        arr = []
        for i in range(len(line)):
          arr.append(int(line[i]))
        end = len(arr) - 1
        result = quickSort(arr, 0, end)
        for j in range(len(result)):
          file2.write(str(result[j]) + " ")
        file2.write("\n")

