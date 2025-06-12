#2(2)


def sortList(file, output):
  n = int(file.readline())
  listN = file.readline().rstrip().split(" ")
  m = int(file.readline())
  listM = file.readline().rstrip().split(" ")
  i = j = 0
  new = []
  while i < n and j < m:
    if int(listN[i]) <= int(listM[j]):
      new += [listN[i]]
      i += 1
    else:
      new += [listM[j]]
      j += 1
  if i != n:
    while i < n:
      new += [listN[i]]
      i += 1
  if j != m:
    while j < m:
      new += [listM[j]]
      j += 1
  for i1 in new:
    output.write(f"{i1} ")
  output.write("\n")



file = open("input2.txt", "r")
output = open("output2b.txt", "w")
for i2 in range(4):
  sortList(file, output)
file.close()
output.close()