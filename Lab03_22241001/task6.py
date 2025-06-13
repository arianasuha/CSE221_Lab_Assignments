def find_elem(arr, k, start = 0, end = 0):
  ind = partition(arr, start, end)
  if ind == k - 1:
    return arr[ind]
  elif ind < k - 1:
    return find_elem(arr, k, ind+1, end)
  elif ind > k - 1:
    return find_elem(arr, k, start, ind-1)
  return -1



def partition(arr, start, end):
  pivot = arr[end]
  pindex = start
  for i in range(start,end):
    if arr[i] <= pivot:
      arr[i], arr[pindex] = arr[pindex], arr[i]
      pindex += 1
  arr[pindex], arr[end] = arr[end], arr[pindex]
  return pindex

with open("input6.txt", "r") as file:
  next(file)
  with open("output6.txt", "w") as file2:
        line = next(file).strip().split()
        arr = []
        for i in range(len(line)):
           arr.append(int(line[i]))
        end = len(arr) - 1
        next(file)
        for lines in file:
           result = find_elem(arr, int(lines), 0, end)
           file2.write(str(result))
           file2.write("\n")


 