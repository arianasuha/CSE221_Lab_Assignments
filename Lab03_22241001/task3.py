def mergeSort(arr):
    if len(arr) == 1:
        return arr, 0
    else:
        mid = len(arr) // 2
        a1 = mergeSort(arr[:mid])   
        a1_arr = a1[0]
        a1_count = a1[1]
        a2 = mergeSort(arr[mid:])
        a2_arr = a2[0]
        a2_count = a2[1]
        count = a1_count + a2_count
        result = merge(a1_arr,a2_arr,count)  
        arr = result[0]
        count = result[1]
        return arr, count
    
def merge(a,b,count):
    i = 0
    j = 0
    new_arr = []
    while i < len(a) and j < len(b):
      if a[i] < b[j]:
        new_arr += [a[i]]
        i += 1  
      else:
        count += len(a) - i
        new_arr += [b[j]]
        j += 1

    if i < len(a):
        new_arr += a[i::]
    if j < len(b):
        new_arr += b[j::]
    return new_arr,count

with open("input3.txt", "r") as file:
  with open("output3.txt", "w") as file2:
     for line in file:
            line = next(file).strip().split()
            arr = []
            for i in range(len(line)):
                arr.append(int(line[i]))
            result = mergeSort(arr)
            file2.write(str(result[1]))
            file2.write("\n")
            
