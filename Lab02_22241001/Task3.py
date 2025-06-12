def max_tasks(file):
  n = file.readline()
  n = int(n)
  tasks1, tasks2 = [], []
  start, end = "", ""
  for i1 in range(n):
    start, end = file.readline().rstrip().split(" ")
    tasks1 += [(start, end)]
  min = 0
  for i2 in range(n-1):
    min = i2
    for i3 in range(i2 + 1, n):
      if int(tasks1[i3][1]) < int(tasks1[min][1]):
        min = i3
    if min != i2:
      tasks1[i2], tasks1[min] = tasks1[min], tasks1[i2]
  tasks2 += [tasks1[0]]
  last = tasks1[0][1]
  for i4 in range(1, n):
    if tasks1[i4][0] >= last:
      tasks2 += [tasks1[i4]]
      last = tasks1[i4][1]
  return len(tasks2), tasks2


file = open("input3.txt", "r")
output = open("output3.txt", "w")
for i in range(3):
  count, intervals = max_tasks(file)
  output.write(str(count) + "\n")
  for i in intervals:
    output.write(str(i[0]) + " " + str(i[1]) + "\n")

file.close()
output.close()