def max_tasks(file, output):
  nums = file.readline().rstrip().split(" ")
  n, m = int(nums[0]), int(nums[1])
  tasks1, tasks2 = [], []
  start, end = "", ""
  for i1 in range(n): # making the list of tasks from file
    start, end = file.readline().rstrip().split(" ")
    tasks1 += [(start, end)]
  min = 0
  for i2 in range(n-1): #sorting the list
    min = i2
    for i3 in range(i2 + 1, n):
      if int(tasks1[i3][1]) < int(tasks1[min][1]):
        min = i3
    if min != i2:
      tasks1[i2], tasks1[min] = tasks1[min], tasks1[i2]
  for i4 in range(m): #setting up list for m number of ppl
    tasks2 += [[]]
  #print(tasks1)
  minL = []
  min = 999
  idx = 0
  for i5 in range(n): #arranging slots
    #print(tasks2)
    minL = []
    min = 999
    idx = -1
    for i6 in range(m):
      if len(tasks2[i6]) == 0:
        tasks2[i6] += [tasks1[i5]]
        break
      elif int(tasks1[i5][0]) == int(tasks2[i6][-1][1]):
        tasks2[i6] += [tasks1[i5]]
        break
      else:
        minL += [int(tasks1[i5][0]) - int(tasks2[i6][-1][1])]
        if i6 == m - 1:
          #print("x", minL)
          for i7 in range(len(minL)):
            #print("x", min, minL[i7])
            if minL[i7] < min and minL[i7] > -1:
              min = minL[i7]
              idx = i7
          if minL[idx] > -1:
            tasks2[idx] += [tasks1[i5]]
          break
  #print(tasks2)
  count = 0
  for i8 in tasks2:
    count += len(i8)
  output.write(str(count) + "\n")


file = open("input4.txt", "r")
output = open("output4.txt", "w")
for i in range(5):
  max_tasks(file, output)

file.close()
output.close()