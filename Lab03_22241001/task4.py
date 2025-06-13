def find_max(arr):
  if len(arr) == 1:
    return arr, 0
  else:
    mid = len(arr) // 2
    left = find_max(arr[:mid])
    l1 = left[0]
    max_l1 = left[1]
    right = find_max(arr[mid:])
    r1 = right[0]
    max_r1 = right[1]
    if max_l1 > max_r1:
      result = merge(l1, r1, max_l1)
    else:
      result = merge(l1, r1, max_r1)
    arr = result[0]
    max = result[1]
    return arr, max

def merge(left, right, max):
  i = 0
  j = 0
  new_arr = []
  while i < len(left) and j < len(right):
    if left[-1] + ((right[j]) ** 2) > max:
      max = left[-1] + ((right[j]) ** 2)
    if left[i] < right[j]:
      new_arr += [left[i]]
      i += 1
    else:
      new_arr += [right[j]]
      j += 1
    
    

  if i < len(left):
    new_arr += left[i:]
  elif j < len(right):
    for items in range(j,len(right)):
      if left[-1] + ((right[items]) ** 2) > max:
        max = left[-1] + ((right[items]) ** 2)
    new_arr += right[j:]
  return new_arr, max

with open("input4.txt", "r") as file:
  with open("output4.txt", "w") as file2:
     for line in file:
            line = next(file).strip().split()
            arr = []
            for i in range(len(line)):
                arr.append(int(line[i]))
            result = find_max(arr)
            file2.write(str(result[1]))
            file2.write("\n")
            



