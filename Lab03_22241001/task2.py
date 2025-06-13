def merge(arr):
  if len(arr) == 1:
    return arr
  else:
    mid = len(arr) // 2
    left_arr = merge(arr[:mid])
    right_arr = merge(arr[mid::])
    return max_find(left_arr, right_arr)

def max_find(left_arr, right_arr):
  if left_arr[0] > right_arr[0]:
    return left_arr
  else:
    return right_arr
  
with open("input2.txt", "r") as file:
  with open("output2.txt", "w") as file2:
     for line in file:
            line = next(file).strip().split()
            arr = []
            for i in range(len(line)):
                arr.append(int(line[i]))
            result = merge(arr)
            file2.write(str(result[0]))
            file2.write("\n")
            