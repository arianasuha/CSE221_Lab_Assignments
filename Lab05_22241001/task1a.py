def dfs(adjL, visited, stack, n, m, v):
  if visited[v] != 1:
    visited[v] = 1
  if len(adjL[v]) != 0:
    for i3 in adjL[v]:
      if visited[i3] == 0:
        dfs(adjL, visited, stack, n, m, i3)
  if v not in stack and visited[v] == 1:
    stack += [v]
    
def cycle_checker(stack, visited, adjL, flag):
  if len(stack) != 0 and flag[0] != True:
    if stack[-1] not in visited:
      visited += [stack[-1]]
    for i4 in adjL[stack[-1]]:
      if i4 not in visited:
        stack += [i4]
        cycle_checker(stack, visited, adjL, flag)
      if i4 in visited and i4 in stack:
        flag[0] = True
        break
    stack.pop()


def adjList(file, n, m):
  adjL = []
  integers = ""
  a = b = 0
  for i1 in range(n + 1):
    adjL += [[]*(n + 1)]
  for i2 in range(m):
    integers = file.readline().rstrip().split(" ")
    a, b = int(integers[0]), int(integers[1])
    adjL[a] += [b]
  return adjL


def course_order(file, output):
  integers = file.readline().rstrip().split(" ")
  n, m = int(integers[0]), int(integers[1])
  adjL = adjList(file, n, m)
  visited = [0] * (n + 1)
  stack = []
  v = 0
  stCyc = []
  flag = [False]
  visC = []
  while v < n and flag[0] == False:
    v += 1
    if v not in visC:
      stCyc = [v]
      visC = [v]
      cycle_checker(stCyc, visC, adjL, flag)
  if flag[0] == True:
    output.write("IMPOSSIBLE")
  else:
    v = 0
    while v < n:
      v += 1
      dfs(adjL, visited, stack, n, m, v)
    while len(stack) != 0:
      output.write(str(stack[-1]) + " ")
      stack.pop()


file1 = open("input1a_1.txt", "r")
output1 = open("output1a_1", "w")
course_order(file1, output1)
file2 = open("input1a_2.txt", "r")
output2 = open("output1a_2", "w")
course_order(file2, output2)
file3 = open("input1a_3.txt", "r")
output3 = open("output1a_3", "w")
course_order(file3, output3)
file1.close()
output1.close()
file2.close()
output2.close()
file3.close()
output3.close()