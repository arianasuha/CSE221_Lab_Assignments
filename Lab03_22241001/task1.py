def mergeSort(arr):
    if len(arr) == 1:
        return arr
    else:
        mid = len(arr) // 2
        a1 = mergeSort(arr[:mid])
        a2 = mergeSort(arr[mid:])
        return merge(a1,a2)
    
def merge(a,b):
    i = 0
    j = 0
    new_arr = []
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            new_arr += [a[i]]
            i += 1  
        else:
            new_arr += [b[j]]
            j += 1

    if i < len(a):
        new_arr += a[i::]
    if j < len(b):
        new_arr += b[j::]
    return new_arr


with open("input1.txt","r") as file:
    with open("output1.txt", "w") as file2:
        for line in file:
            line = next(file).strip().split()
            arr = []
            for i in range(len(line)):
                arr.append(int(line[i]))
            result = mergeSort(arr)
            for items in result:
                file2.write(str(items) + " ")
            file2.write("\n")


